import unittest
import pandas as pd
from etl.load import load_data
import sqlalchemy

class TestLoad(unittest.TestCase):

    def setUp(self):
        self.df = pd.DataFrame({'column1': [1, 2, 3], 'column2': ['a', 'b', 'c']})
        self.config = {
            'db_connection_string': 'sqlite:///:memory:',
            'destination_table': 'test_table'
        }

    def test_load_data(self):
        engine = sqlalchemy.create_engine(self.config['db_connection_string'])
        load_data(self.df, self.config)
        result = engine.execute("SELECT * FROM test_table").fetchall()
        self.assertEqual(len(result), 3)

if __name__ == '__main__':
    unittest.main()
