from preprocessing.feature_extraction.document_cleaning import DocumentCleaning

import unittest


class BasicTestSuite(unittest.TestCase):

    def test_map_to_stemmed_words(self):
        document = "Ein Hase isst Möhren. Er mag den Frühling. Er sagt: »Hallo Welt!«"
        cleaning = DocumentCleaning(document)
        actual_words = cleaning.map_to_stemmed_words()
        expected_words = ['ein', 'has', 'isst', 'mohr', 'er', 'mag', 'fruhling', 'er', 'sagt', 'hallo', 'welt']
        self.assertEqual(expected_words, actual_words)

        cleaning = DocumentCleaning(document, False)
        actual_words = cleaning.map_to_stemmed_words()
        expected_words = ['ein', 'has', 'isst', 'mohr', '.', 'er', 'mag', 'den', 'fruhling', '.',
                          'er', 'sagt', ':','``', 'hallo', 'welt', '!', "''"]
        self.assertEqual(expected_words, actual_words)

    def test_map_to_sentece_length(self):
        document = "Ein Hase isst Möhren. Er mag den Frühling. Er sagt: »Hallo Welt!«"
        cleaning = DocumentCleaning(document)
        actual_lengths = cleaning.map_to_sentence_length()
        expected_lengths = [21, 20, 22]
        self.assertEqual(expected_lengths, actual_lengths)

        cleaning = DocumentCleaning(document, False)
        actual_lengths = cleaning.map_to_sentence_length()
        self.assertEqual(expected_lengths, actual_lengths)

if __name__ == '__main__':
        unittest.main()