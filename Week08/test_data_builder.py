import unittest
from data_builder import DataBuilder

class TestDataBuilder(unittest.TestCase):
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
            'a1': 1,
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

    def test_when_an_empty_dict_is_given_return_empty_list_dfs(self):
        db_obj = DataBuilder({})
        expexted_result = []
        self.assertEqual(db_obj.dfs(), expexted_result)

    def test_when_simple_dict_is_given_return_dfs_struct(self):
        db_obj = DataBuilder(self.simple_dict)
        expexted_result = [('a', 1), ('b', 2)]
        self.assertEqual(db_obj.dfs(), expexted_result)

    def test_when_list_with_dicts_is_given_return_dfs_struct(self):
        db_obj = DataBuilder(self.list_with_dicts)
        expexted_result = [('a', 1), ('b', 2)]
        self.assertEqual(db_obj.dfs(), expexted_result)

    def test_when_nested_dicts_is_given_return_dfs_struct(self):
        db_obj = DataBuilder(self.nested_dicts)
        expexted_result = [('a', {'a1': 1, 'a2': 2}), ('a1', 1), ('a2', 2), 
                           ('b', {'b1': 1}), ('b1', 1)]
        self.assertEqual(db_obj.dfs(), expexted_result)

    def test_when_nested_dicts_with_lists_is_given_return_dfs_struct(self):
        db_obj = DataBuilder(self.nested_dicts_with_lists)
        expecte_result = [('a', {'a1': [{'a11': 11}], 'a2': [1, 2]}), ('a1', [{'a11': 11}]), 
                          ('a11', 11), ('a2', [1, 2]), 
                          ('b', {'b1': [{'b11': 11}, {'b12': 12}]}), 
                          ('b1', [{'b11': 11}, {'b12': 12}]), ('b11', 11), ('b12', 12)]
        self.assertEqual(db_obj.dfs(), expecte_result)

    # ------------------------------- BFS tests ----------------------------------
    
    def test_when_an_empty_dict_is_given_return_empty_list_bfs(self):
        db_obj = DataBuilder({})
        expexted_result = []
        self.assertEqual(db_obj.dfs(), expexted_result)

    def test_when_simple_dict_is_given_return_bfs_struct(self):
        db_obj = DataBuilder(self.simple_dict)
        expexted_result = [('a', 1), ('b', 2)]
        self.assertEqual(db_obj.bfs(), expexted_result)

    def test_when_list_with_dicts_is_given_return_bfs_struct(self):
        db_obj = DataBuilder(self.list_with_dicts)
        expexted_result = [('a', 1), ('b', 2)]
        self.assertEqual(db_obj.bfs(), expexted_result)

    def test_when_nested_dicts_is_given_return_bfs_struct(self):
        db_obj = DataBuilder(self.nested_dicts)
        expexted_result = [('a', {'a1': 1, 'a2': 2}), ('b', {'b1': 1}), 
                           ('a1', 1), ('a2', 2), ('b1', 1)]
        self.assertEqual(db_obj.bfs(), expexted_result)

    def test_when_nested_dicts_with_lists_is_given_return_bfs_struct(self):
        db_obj = DataBuilder(self.nested_dicts_with_lists)
        expecte_result = [('a', {'a1': [{'a11': 11}], 'a2': [1, 2]}), 
                          ('b', {'b1': [{'b11': 11}, {'b12': 12}]}), 
                          ('a1', [{'a11': 11}]), ('a2', [1, 2]), 
                          ('b1', [{'b11': 11}, {'b12': 12}]), 
                          ('a11', 11), 
                          ('b11', 11), ('b12', 12)]
        self.assertEqual(db_obj.bfs(), expecte_result)


if __name__ == "__main__":
    unittest.main()