from preprocessing.feature_extraction.document_cleaning import DocumentCleaning
from preprocessing.feature_extraction.vectorization import Vectorization


collections = ['grimm', 'andersen', 'dietrich', 'wilhelm', 'bechstein', 'alberti', 'ruland']

vectorization = Vectorization(matrix_shape=(5000, 1000), growth_words=500, growth_docs=50)
for collection_name in collections:
    print('reading', collection_name, '...')
    path = '../../data/collections/collection_'+collection_name+'.txt'
    collection = {}
    with open(path, 'r') as f:
        for line in f:
            doc_hash = eval(line.split('\t')[1])
            key = collection_name + '#' + doc_hash['headline']
            collection[key] = doc_hash['text'].strip()

    print('processing', collection_name, '(#fairy tales:', len(collection), ')...')
    for headline, document in collection.items():
        cleaning = DocumentCleaning(document)
        lengths = cleaning.map_to_sentence_length()
        vectorization.add_sentence_length_vector(lengths, headline)
        words_in_document = cleaning.map_to_stemmed_words()
        vectorization.add_document(words_in_document, headline)

path = '../../data/vectorization/'
name = str(collections).replace('[', '').replace(']', '').replace('\'', '').replace(', ', '_')
print('calculating TF/IDF and exporting data to', path, '...')
vectorization.export_results(path, name)

