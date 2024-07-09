
from indra_cogex.sources.odinson.grammars import Rule
from indra_cogex.sources.odinson.client import process_rules
import gilda
import pandas as pd
from collections import defaultdict
from gilda.process import normalize
from pyobo.gilda_utils import get_gilda_terms


spine_file = '/Users/sangeethavempati/Documents/GitHub/reach/bioresources/src/main/resources/org/clulab/reach/kb/spine.tsv'
#reformat terms
df = pd.read_csv(spine_file, sep='\t', header=None, names=['name', 'id'])
#for each id, make a list of the corresponding brain regions
id_to_names = defaultdict(list)
for name,identifier in df.values:
    id_to_names[identifier].append(name)
terms = []
#label terms with the same id as synonyms
for identifier, names in id_to_names.items():
    #label everything except the first as synonyms
    name,*synonyms = names
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
#terms.extend(get_gilda_terms('ncit'))
grounder = gilda.Grounder(terms)
grounder
