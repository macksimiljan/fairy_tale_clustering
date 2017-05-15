from time import sleep

from preprocessing.request.document_request import DocumentRequestGrimm


class CollectionRequest(object):

    def __init__(self, url, collection_name):
        if len(url) < 1:
            raise ValueError('URL cannot be empty!')
        self.__url = url
        self.__collection_name = collection_name
        self.__pages_per_collection = {'grimm': (4, 204), 'andersen': (2, 113),
                                       'alberti': (3, 26), 'bechstein': (2, 48),
                                       'dietrich': (4, 20), 'gelber': (2, 28),
                                       'wilhelm': (3, 102), 'wenzig': (2, 35),
                                       'ruland': (3, 81)}
        self.__locking_per_collection = {'grimm': 10, 'andersen': 10,
                                         'alberti': 5, 'bechstein': 7,
                                         'dietrich': 7, 'gelber': 7,
                                         'wilhelm': 10, 'wenzig': 7,
                                         'ruland': 10}

    def run_scraping(self):
        pages = self.__pages_per_collection[self.__collection_name]
        start_page = pages[0]
        end_page = pages[1]
        locking = self.__locking_per_collection[self.__collection_name]

        documents = {}
        for p in range(start_page, end_page + 1):
            documents[p] = self.__query_document(p)
            sleep(locking)
        return documents

    def __query_document(self, page):
        document = {}
        try:
            document_url = self.__url + '/' + str(page)
            print(document_url)
            request = DocumentRequestGrimm(document_url)
            headline = request.get_headline()
            text = request.get_text()
            document = {'headline': headline, 'text': text}
        except Exception:
            print('Error for page', page, '!')

        return document
