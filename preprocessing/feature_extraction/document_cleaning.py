from re import search as regexp_search
import nltk
from nltk.stem.snowball import GermanStemmer
from nltk.tokenize import word_tokenize, sent_tokenize


class DocumentCleaning(object):

    __LANG = 'german'

    def __init__(self, document, stopword_filter=True):
        self.__stopwords = set(nltk.corpus.stopwords.words(DocumentCleaning.__LANG))
        self.__document = self.__replace_quotation_marks(document)
        self.__stopword_filter = stopword_filter
        self.__sentences = sent_tokenize(self.__document, DocumentCleaning.__LANG)

    def map_to_stemmed_words(self):
        cleaned_document = []
        for sentence in self.__sentences:
            stemmed_sentence = self.__tokenize_and_stem(sentence)
            cleaned_document.extend(stemmed_sentence)
        return cleaned_document

    def map_to_sentence_length(self):
        return [len(sentence) for sentence in self.__sentences]

    def __replace_quotation_marks(self, document):
        d = document.replace('»', '\"')
        return d.replace('«', '\"')

    def __tokenize_and_stem(self, sentence):
        filtered_stems = []
        stemmer = GermanStemmer()
        tokens = word_tokenize(sentence)
        for token in tokens:
            if self.__stopword_filter and self.__is_stopword(token):
                pass
            else:
                stem = stemmer.stem(token)
                filtered_stems.append(stem)
        return filtered_stems

    def __is_stopword(self, word):
        return word in self.__stopwords or regexp_search('\w', word) is None
