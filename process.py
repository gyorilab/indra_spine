import csv
import json
import os.path
import itertools
import pickle
from collections import defaultdict

import tqdm
import pystow
from indra.literature import pubmed_client
from indra_cogex.sources.odinson.document import process_document

base = pystow.module('neuroimg')

search_terms = ['fatigue']


def get_pmids(search_terms):
    fname = base.join(name='pmids.txt')
    if not fname.exists():
        pmids = set()
        for search_term in search_terms:
            pmids |= set(pubmed_client.get_ids(search_term))
        pmids = sorted(pmids)
        with open(fname, 'w') as fh:
            fh.write('\n'.join(pmids))
    else:
        with open(fname, 'r') as fh:
            pmids = [l.strip() for l in fh.readlines()]
    return pmids


def get_content(pmids):
    from indra_db_lite import get_plaintexts_for_text_ref_ids, \
       get_text_ref_ids_for_pmids
    for pmid in tqdm.tqdm(pmids, desc='Getting text content'):
        mappings = get_text_ref_ids_for_pmids([int(pmid)])
        if int(pmid) in mappings:
            trid = mappings[int(pmid)]
            text_content = get_plaintexts_for_text_ref_ids([trid])
            if not text_content:
                continue
            _, content = next(text_content.trid_content_pairs())
            if content:
                fname = base.join('text', name=f'{pmid}.txt')
                with open(fname, 'w') as fh:
                    fh.write(content)


def ontology_to_tsv():
    fname = base.join(name='ontology_thalamus_freesurfer_thomas.json')
    rows = []
    with open(fname, 'r') as fh:
        entries = json.load(fh)
        for entry in entries:
            variants = [entry['label'], entry['label'].replace('-', ' ')]
            for variant in variants:
                rows.append((variant,
                             entry['ontologyClassIri'].split('/')[-1]))
    fname = os.path.join(os.path.expanduser('~'), 'src',  'reach',
                         'bioresources', 'src', 'main', 'resources', 'org',
                         'clulab', 'reach', 'kb', 'spine.tsv')
    with open(fname, 'w') as fh:
        writer = csv.writer(fh, delimiter='\t')
        writer.writerows(rows)


def ontology_to_grounder():
    from gilda.term import Term
    from gilda.process import normalize
    from gilda.grounder import Grounder
    fname = base.join(name='ontology_thalamus_freesurfer_thomas.json')
    terms = []
    with open(fname, 'r') as fh:
        entries = json.load(fh)
        for entry in entries:
            variants = [entry['label'], entry['label'].replace('-', ' ')]
            for variant in variants:
                term = Term(normalize(variant), variant, 'SPINE',
                            entry['ontologyClassIri'].split('/')[-1],
                            entry['label'], 'synonym', 'spine')
                terms.append(term)
    grounder = Grounder(terms)
    return grounder


def ontology_name_lookup():
    fname = base.join(name='ontology_thalamus_freesurfer_thomas.json')
    lookup = {}
    with open(fname, 'r') as fh:
        entries = json.load(fh)
        for entry in entries:
            id = entry['ontologyClassIri'].split('/')[-1]
            name = entry['label']
            lookup[id] = name
    return lookup


def get_agents():
    agents_pkl = base.join(name='agents.pkl')
    if not agents_pkl.exists():
        print('Processing documents de novo')
        grounder = ontology_to_grounder()
        agents = {}
        for fname in tqdm.tqdm(list(base.join('docs').glob('*.json.gz'))):
            pmid = os.path.splitext(fname)[0]
            doc = process_document(fname)
            doc_agents = doc.get_grounded_agents(grounder=grounder.ground)
            agents[pmid] = doc_agents
        with open(agents_pkl, 'wb') as fh:
            pickle.dump(agents, fh)
    else:
        print('Loading agents from pickle')
        with open(agents_pkl, 'rb') as fh:
            agents = pickle.load(fh)
    return agents


def get_network_edges(agents):
    blacklist = {'Background'}
    lookup = ontology_name_lookup()
    network = defaultdict(list)
    for doc_path, doc_agents in agents.items():
        pmid = os.path.splitext(os.path.basename(doc_path))[0]
        groundings = {a.db_refs['SPINE'] for a in doc_agents if
                      'SPINE' in a.db_refs}
        for a, b in itertools.combinations(groundings, 2):
            aname = lookup[a]
            bname = lookup[b]
            if aname in blacklist or bname in blacklist:
                continue
            network[tuple(sorted([aname, bname]))].append(pmid)
    return network


def get_nice_cx_network(network_edges):
    from ndex2.nice_cx_network import NiceCXNetwork
    network = NiceCXNetwork()
    context_prefixes = {
        'pubmed': 'https://identifiers.org/pubmed:',
    }
    network.set_network_attribute('@context',
                                  json.dumps(context_prefixes))
    network.set_network_attribute('name', 'Fatigue anatomy network')
    node_keys = {}
    edge_citations = {}
    for (a, b), pmids in network_edges.items():
        akey = node_keys[a] if a in node_keys else network.create_node(a)
        node_keys[a] = akey
        bkey = node_keys[b] if b in node_keys else network.create_node(b)
        node_keys[b] = bkey
        ekey = network.create_edge(akey, bkey)
        edge_citations[ekey] = len(pmids)
        pmids_attr = ['pubmed:%s' % pmid for pmid in pmids]
        network.set_edge_attribute(ekey, 'citations', pmids_attr,
                                   type='list_of_string')
        network.set_edge_attribute(ekey, 'name', '(%s)-(%s)' % (a, b))
    saturation = 20
    for edge, ncitations in edge_citations.items():
        weight = 1 + 9 * (min(ncitations-1, saturation) / saturation)
        network.set_edge_attribute(edge, 'weight', weight)
    return network


def upload_network(ncx):
    from indra.databases import ndex_client
    username, password = ndex_client.get_default_ndex_cred({})
    ndex_args = {'username': username,
                 'password': password,
                 'server': 'http://public.ndexbio.org'}
    ncx.upload_to(**ndex_args)


if __name__ == '__main__':
    # Step 1: Get PMIDs based on search terms
    pmids = get_pmids(search_terms)

    # Step 2: Get text content for PMIDs and write these into an appropriate
    # folder
    get_content(pmids)

    # Step 3: Convert the ontology terms into a Reach bioresource file
    ontology_to_tsv()

    # Step 4: If ontology terms changed, we need to rebuild Reach
    # cd ~/src/reach
    # sbt publishLocal

    # Step 5: run Odinson annotation on the text content
    # cd ~/src/odinson
    # ./annotate.sh

    # Step 6: Process annotated documents and get agents out
    agents = get_agents()

    # Step 7: Construct a network from the agents
    network_edges = get_network_edges(agents)

    # Step 8: Convert the network to a nice CX network
    ncx = get_nice_cx_network(network_edges)

    # Step 9: Upload the network to NDEx
    upload_network(ncx)
