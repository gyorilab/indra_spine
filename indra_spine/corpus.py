import os

from indra_db import get_db
from indra_db.client.principal.content import get_text
from indra.literature import pubmed_client


def get_ids(term):
    # get a list of pubmed IDs for the search term
    ids = pubmed_client.get_all_ids(term)
    return ids


def make_text_folder(path, term, ids):
    absolute_path = os.path.abspath(os.path.expanduser(os.path.join(path, term, 'text')))
    os.makedirs(absolute_path, exist_ok=True)
    os.chdir(absolute_path)

    db = get_db('primary')
    text = get_text(db, ids, 'abstract')

    for pmid,content in text.items():
        with open('{}.txt'.format(pmid),'w') as file:
            file.write(content)
