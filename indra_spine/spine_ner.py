import os
import sys
from collections import defaultdict

import pandas as pd
import gilda
from gilda.process import normalize
from pyobo.gilda_utils import get_gilda_terms
from indra_cogex.sources.odinson.grammars import Rule
from indra_cogex.sources.odinson.client import process_rules


def get_spine_grounder():
    # Get the REACH_HOME environment variable
    reach_home = os.environ.get('REACH_HOME')

    if not reach_home:
        raise EnvironmentError("REACH_HOME is not set in "
                               "environment variables.")

    # Example of using REACH_HOME in the path
    spine_file = os.path.join(reach_home, 'bioresources', 'src', 'main',
                              'resources', 'org', 'clulab', 'reach', 'kb',
                              'spine.tsv')

    # Reformat terms
    df = pd.read_csv(spine_file, sep='\t', header=None, names=['name', 'id'])
    # For each id, make a list of the corresponding brain regions
    id_to_names = defaultdict(list)
    for name, identifier in df.values:
        id_to_names[identifier].append(name)
    terms = []
    # Label terms with the same id as synonyms
    for identifier, names in id_to_names.items():
        # Label everything except the first as synonyms
        name, *synonyms = names
        term = gilda.term.Term(
                    norm_text=normalize(name),
                    text=name,
                    db="spine",
                    id=identifier,
                    entry_name=name,
                    status="name",
                    source="spine",
                )
        terms.append(term)
        for synonym in synonyms:
            term = gilda.term.Term(
                    norm_text=normalize(synonym),
                    text=synonym,
                    db="spine",
                    id=identifier,
                    entry_name=name,
                    status="synonym",
                    source="spine",
                )
            terms.append(term)
    terms.extend(get_gilda_terms('UBERON'))
    terms.extend(get_gilda_terms('fma'))
    grounder = gilda.Grounder(terms)
    return grounder