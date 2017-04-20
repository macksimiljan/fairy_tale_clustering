from preprocessing.document_request import DocumentRequestGrimm
from preprocessing.collection_request import CollectionRequest

r = CollectionRequest('http://gutenberg.spiegel.de/buch/kinder-und-hausmarchen-7018', 'grimm')
grimm_documents = r.run_scraping()
with open("collection_grimm.txt", "w") as file:
    for document in grimm_documents:
        line = str(document) + '\t' + str(grimm_documents[document]) + '\n'
        file.write(line)

