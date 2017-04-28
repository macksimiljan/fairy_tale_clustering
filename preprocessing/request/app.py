from preprocessing.request.collection_request import CollectionRequest

collections = {'grimm': 'http://gutenberg.spiegel.de/buch/kinder-und-hausmarchen-7018',
               'andersen': 'http://gutenberg.spiegel.de/buch/sammtliche-marchen-einzige-vollstandige-vom-verfasser-besorgte-ausgabe-6246',
               'dietrich': 'http://gutenberg.spiegel.de/buch/russische-volksmarchen-4999',
               'gelber': 'http://gutenberg.spiegel.de/buch/negermarchen-6909',
               'wilhelm': 'http://gutenberg.spiegel.de/buch/chinesische-marchen-6252',
               'bechstein': 'http://gutenberg.spiegel.de/buch/marchen-7468',
               'alberti': 'http://gutenberg.spiegel.de/buch/japanische-marchen-2426'}

current_collection_name = 'andersen'
print('Collection:', current_collection_name)
r = CollectionRequest(collections[current_collection_name], current_collection_name)
documents = r.run_scraping()
file_path = '../data/collections/collection_' + current_collection_name + ".txt"
with open(file_path, "w") as file:
    for document in documents:
        line = str(document) + '\t' + str(documents[document]) + '\n'
        file.write(line)
        

