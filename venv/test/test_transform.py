import unittest
import pandas as pd
from etl.transform import transform_data

class TestTransform(unittest.TestCase):

    def setUp(self):
        self.df = pd.DataFrame({
            'old_name': ['value1', 'value2', 'value3'],
            'filter_column': ['filter_value', 'other_value', 'filter_value']
        })
        self.config = {
            'columns_to_rename': {'old_name': 'new_name'},
            'filter_conditions': {'filter_column': 'filter_value'}
        }

    def test_transform_data(self):
        transformed_df = transform_data(self.df, self.config)
        self.assertIn('new_name', transformed_df.columns)
        self.assertNotIn('old_name', transformed_df.columns)
        self.assertEqual(len(transformed_df), 2)

if __name__ == '__main__':
    unittest.main()
