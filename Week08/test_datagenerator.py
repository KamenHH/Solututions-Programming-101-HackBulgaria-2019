import unittest
from data_builder import DataGenerator


class TestDataGenerator(unittest.TestCase):
    # ------- test data -------

    simple_dict = {
        'a': 1,
        'b': 2
    }

    list_with_dicts = [
        {'a' : 1},
        {'b' : 2}
    ]

    nested_dicts = {
        'a': {
            'a1': {
                'a11' : 11
            },
            'a2': 2
        },
        'b': {
            'b1': 1
        }
    }


    nested_dicts_with_lists = {
        'a': {
            'a1': [
                {
                    'a11': 11
                }
            ],
            'a2': [1, 2]
        },
        'b': {
            'b1': [
                {
                    'b11': 11
                },
                {
                    'b12': 12
                }
            ]
        }
    }

    # ------------------------------- DFS tests ----------------------------------

    def test_when_an_empty_dict_is_given_return_list_with_empty_dict_dfs(self):
        db_obj = DataGenerator({})
        expexted_result = [{}]
        self.assertEqual(list(db_obj.dfs()), expexted_result)

    def test_when_simple_dict_is_given_return_result_dfs(self):
        db_obj = DataGenerator(self.simple_dict)
        expexted_result = [{'a' : 1, 'b': 2}]
        self.assertEqual(list(db_obj.dfs()), expexted_result)

    def test_when_list_with_dicts_is_given_return_result_dfs(self):
        db_obj = DataGenerator(self.list_with_dicts)
        expexted_result = [{'a': 1}, {'b': 2}]
        self.assertEqual(list(db_obj.dfs()), expexted_result)

    def test_when_nested_dicts_is_given_return_result_dfs(self):
        db_obj = DataGenerator(self.nested_dicts)
        expexted_result = [{'a': {'a1': {'a11': 11}, 'a2': 2}, 'b': {'b1': 1}}, 
                           {'a1': {'a11': 11}, 'a2': 2}, 
                           {'a11': 11}, 
                           {'b1': 1}]
        self.assertEqual(list(db_obj.dfs()), expexted_result)

    def test_when_nested_dicts_with_lists_is_given_return_result_dfs(self):
        db_obj = DataGenerator(self.nested_dicts_with_lists)
        expecte_result = [{'a': {'a1': [{'a11': 11}], 'a2': [1, 2]}, 'b': {'b1': [{'b11': 11}, {'b12': 12}]}},
                          {'a1': [{'a11': 11}], 'a2': [1, 2]},
                          {'a11': 11},
                          {'b1': [{'b11': 11}, {'b12': 12}]},
                          {'b11': 11},
                          {'b12': 12}]
        self.assertEqual(list(db_obj.dfs()), expecte_result)

    # ------------------------------- BFS tests ----------------------------------
    
    def test_when_an_empty_dict_is_given_return_list_with_empty_dict_bfs(self):
        db_obj = DataGenerator({})
        expexted_result = [{}]
        self.assertEqual(list(db_obj.dfs()), expexted_result)

    def test_when_simple_dict_is_given_return_result_bfs(self):
        db_obj = DataGenerator(self.simple_dict)
        expexted_result = [{'a' : 1, 'b': 2}]
        self.assertEqual(list(db_obj.bfs()), expexted_result)

    def test_when_list_with_dicts_is_given_return_result_bfs(self):
        db_obj = DataGenerator(self.list_with_dicts)
        expexted_result = [{'a': 1}, {'b': 2}]
        self.assertEqual(list(db_obj.bfs()), expexted_result)

    def test_when_nested_dicts_is_given_return_result_bfs(self):
        db_obj = DataGenerator(self.nested_dicts)
        expexted_result = [{'a': {'a1': {'a11': 11}, 'a2': 2}, 'b': {'b1': 1}},
                           {'a1': {'a11': 11}, 'a2': 2},
                           {'b1': 1},
                           {'a11': 11}]
        self.assertEqual(list(db_obj.bfs()), expexted_result)

    def test_when_nested_dicts_with_lists_is_given_return_result_bfs(self):
        db_obj = DataGenerator(self.nested_dicts_with_lists)
        expected_result = [{'a': {'a1': [{'a11': 11}], 'a2': [1, 2]}, 'b': {'b1': [{'b11': 11}, {'b12': 12}]}},
                           {'a1': [{'a11': 11}], 'a2': [1, 2]},
                           {'b1': [{'b11': 11}, {'b12': 12}]},
                           {'a11': 11},
                           {'b11': 11},
                           {'b12': 12}]
        self.assertEqual(list(db_obj.bfs()), expected_result)


if __name__ == "__main__":
    unittest.main()