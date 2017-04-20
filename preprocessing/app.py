from preprocessing.collection_request import CollectionRequest

collections = {'grimm': 'http://gutenberg.spiegel.de/buch/kinder-und-hausmarchen-7018',
               'andersen': 'http://gutenberg.spiegel.de/buch/sammtliche-marchen-einzige-vollstandige-vom-verfasser-besorgte-ausgabe-6246'}

current_collection_name = 'andersen'
r = CollectionRequest(collections[current_collection_name], current_collection_name)
documents = r.run_scraping()
file_path = '../data/collections/collection_' + current_collection_name + ".txt"
with open(file_path, "w") as file:
    for document in documents:
        line = str(document) + '\t' + str(documents[document]) + '\n'
        file.write(line)

