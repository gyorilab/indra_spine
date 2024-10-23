import os

from indra_db import get_db
from indra_db.client.principal.content import get_text
from indra.literature import pubmed_client


def get_ids(term):
    # get a list of pubmed IDs for the search term
    ids = pubmed_client.get_all_ids(term)
    return ids


def make_text_folder(term, ids):
    # TODO: this should be in a folder path that the user selects, not inside the package
    os.makedirs(term + '/text', exist_ok=True)
    os.chdir(term + '/text')

    db = get_db('primary')
    text = get_text(db, ids, 'abstract')

    for pmid,content in text.items():
        with open('{}.txt'.format(pmid),'w') as file:
            file.write(content)
