from preprocessing.feature_extraction.lexicon import Lexicon

from numpy import int16, pad, round, zeros
from sklearn.feature_extraction.text import TfidfTransformer


class Vectorization(object):

    def __init__(self, matrix_shape=(3000, 100), matrix_extension_words=500, matrix_extension_docs=50):
        self.__matrix = zeros(matrix_shape, dtype=int16)
        self.__lexicon_words = Lexicon()
        self.__lexicon_doc = Lexicon()
        self.__fairy_tale_counter = 0
        self.__matrix_extension_words = matrix_extension_words
        self.__matrix_extension_docs = matrix_extension_docs

    def add_document(self, words, document_name='fairy tale'):
        doc_id = self.__lexicon_doc.add_entry(document_name + ' #' + str(self.__fairy_tale_counter))
        self.__fairy_tale_counter += 1
        for word in words:
            word_id = self.__lexicon_words.add_entry(word)
            self.__add_word_to_matrix(word_id, doc_id)

    def __add_word_to_matrix(self, word_id, doc_id):
        self.__adjust_matrix_size(word_id, doc_id)
        previous_frequency = self.__matrix[word_id, doc_id]
        new_frequency = previous_frequency + 1
        self.__matrix[word_id, doc_id] = new_frequency

    def __adjust_matrix_size(self, word_id, doc_id):
        row_count = self.__matrix.shape[0]
        column_count = self.__matrix.shape[1]
        if word_id >= row_count:
            self.__add_further_rows()
        if doc_id >= column_count:
            self.__add_further_column()

    def __add_further_rows(self):
        extension = ((0, self.__matrix_extension_words), (0, 0))
        self.__matrix = pad(self.__matrix, extension, 'constant', constant_values = (0))

    def __add_further_column(self):
        extension = ((0, 0), (0, self.__matrix_extension_docs))
        self.__matrix = pad(self.__matrix, extension, 'constant', constant_values=(0))

    def get_count_matrix(self):
        number_documents = len(self.__lexicon_doc)
        number_words = len(self.__lexicon_words)
        return self.__matrix[:number_words, :number_documents]

    def print_count_matrix(self, minimum_word_frequency=1):
        number_documents = len(self.__lexicon_doc)
        number_words = len(self.__lexicon_words)
        header = '{:20}'.format(' ')
        for doc_label_id in range(0, number_documents):
            header += '{:15}'.format(self.__lexicon_doc.get_entry(doc_label_id))
        print(header)
        for word_id in range(0, number_words):
            row = '{:20}'.format(self.__lexicon_words.get_entry(word_id))
            word_frequency = 0
            for doc_id in range(0, number_documents):
                freq = self.__matrix[word_id, doc_id]
                word_frequency += freq
                row += '{:15}'.format(str(freq))
            if word_frequency >= minimum_word_frequency:
                print(row)

    def write_count_matrix(self, path, minimum_word_frequency=1):
        number_documents = len(self.__lexicon_doc)
        number_words = len(self.__lexicon_words)
        with open(path, "w") as file:
            header = ''
            for doc_label_id in range(0, number_documents):
                header += '\t' + self.__lexicon_doc.get_entry(doc_label_id)
            file.write(header + '\n')
            for word_id in range(0, number_words):
                row = self.__lexicon_words.get_entry(word_id)
                word_frequency = 0
                for doc_id in range(0, number_documents):
                    freq = self.__matrix[word_id, doc_id]
                    word_frequency += freq
                    row += '\t' + str(freq)
                if word_frequency >= minimum_word_frequency:
                    file.write(row + '\n')

    def get_tfidf_matrix(self):
        number_documents = len(self.__lexicon_doc)
        number_words = len(self.__lexicon_words)
        matrix =  self.__matrix[:number_words, :number_documents]
        inverse_matrix = matrix.transpose()
        transformer = TfidfTransformer()
        tfidf = transformer.fit_transform(inverse_matrix)
        return round(tfidf.toarray(), 3)
