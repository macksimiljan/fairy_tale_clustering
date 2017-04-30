from preprocessing.feature_extraction.vectorization import Vectorization

from numpy.testing import assert_almost_equal, assert_array_equal
import unittest


class BasicTestSuite(unittest.TestCase):

    def test_get_count_matrix(self):
        collection = (['ein', 'hase', 'isst', 'möhren', 'er', 'isst', 'gerne'],
                      ['ein', 'huhn', 'isst', 'keine', 'möhren'])
        expected_matrix = [[1, 1],  # ein
                           [1, 0],  # hase
                           [2, 1],  # isst
                           [1, 1],  # möhren
                           [1, 0],  # er
                           [1, 0],  # gerne
                           [0, 1],  # huhn
                           [0, 1]]  # keine

        vectorization = Vectorization(matrix_shape=(20,2))
        for document in collection:
            vectorization.add_document(document)
        count_matrix = vectorization.get_count_matrix()
        assert_array_equal(expected_matrix, count_matrix)

        vectorization = Vectorization(matrix_shape=(1, 1))
        for document in collection:
            vectorization.add_document(document)
        count_matrix = vectorization.get_count_matrix()
        assert_array_equal(expected_matrix, count_matrix)

        # TODO: test performance for different initial matrix shapes

    def test_get_tfidf_matrix(self):
        collection = (['ein', 'hase', 'isst', 'möhren', 'er', 'isst', 'gerne'],
                      ['ein', 'huhn', 'isst', 'keine', 'möhren'])
        expected_matrix = [[0.290, 0.407, 0.579, 0.290, 0.407, 0.407, 0.000, 0.000],
                           [0.379, 0.000, 0.379, 0.379, 0.000, 0.000, 0.533, 0.533]]

        vectorization = Vectorization(matrix_shape=(20, 2))
        for document in collection:
            vectorization.add_document(document)
        tfidf_matrix = vectorization.get_tfidf_matrix()
        assert_almost_equal(expected_matrix, tfidf_matrix)


if __name__ == '__main__':
        unittest.main()
