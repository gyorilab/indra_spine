from indra_db import get_db
from indra_db.client.principal.content import get_text

import os
from indra.literature import pubmed_client


def main():

    #get a list of pubmed IDs for the search term
    test = pubmed_client
    ids = pubmed_client.get_all_ids('ataxia')
    
    print(len(ids))

    os.makedirs('test_corpus', exist_ok=True)
    os.chdir('test_corpus')

    db = get_db('primary')
    text = get_text(db, ids[:10], 'abstract')

    for pmid,content in text.items():
        with open('{}.txt'.format(pmid),'w') as file:
            file.write(content)

if __name__ == "__main__":
    main()
