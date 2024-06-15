import unittest
from etl.extract import extract_data

class TestExtract(unittest.TestCase):

    def setUp(self):
        self.config = {
            's3_bucket': 'my-test-bucket',
            's3_key': 'data/test_data.csv'
        }

    def test_extract_data(self):
        df = extract_data(self.config)
        self.assertIsNotNone(df)
        self.assertGreater(len(df), 0)

if __name__ == '__main__':
    unittest.main()
