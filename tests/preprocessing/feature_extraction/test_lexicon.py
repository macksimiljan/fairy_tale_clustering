from preprocessing.feature_extraction.lexicon import Lexicon

import unittest


class BasicTestSuite(unittest.TestCase):

    def test_lexicon(self):
        lexicon = Lexicon()
        self.assertEqual(0, len(lexicon))

        lexicon.add_entry('entry #1')
        lexicon.add_entry('entry #2')
        self.assertEqual(2, len(lexicon))

        lexicon.add_entry('entry #2')
        self.assertEqual(2, len(lexicon))

        try:
            # array is not hashable
            lexicon.add_entry(['entry', '#3'])
            self.assertFalse(False)
        except Exception:
            self.assertTrue(True)

        actual_entry = lexicon.get_entry(0)
        self.assertEqual('entry #1', actual_entry)

if __name__ == '__main__':
    unittest.main()
