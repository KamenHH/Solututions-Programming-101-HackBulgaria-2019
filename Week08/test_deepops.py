import unittest
from deepops import DeepOps
from datagenerator import DataGenerator


class TestDeepOps(unittest.TestCase):
    def setUp(self):
        self.simple_dict = {'a': 1, 'b': 2}

        self.nested_dicts = {
            'a': {
                'a': 1,
                'b': {
                    'a': 3
                }
            },
            'b': {
                'b': 2
            }
        }

        self.simple_list_with_dict = [{'a': 1, 'b': 2}]

        self.nested_dicts_and_lists = [
            {
                'a': 1,
                'b': [
                    {
                        'a' : 2
                    }
                ]
            },
            {
                'b' : [
                    {'b': 2}
                ]
            }
        ]

    # ----------------------- DFS TESTS --------------------------
    # -------------------- deep_find DFS tests -------------------

    def test_deep_find_with_simple_dict_dfs(self):
        do_obj = DeepOps(self.simple_dict)
        expected_result = 1
        self.assertEqual(do_obj.deep_find('a'), expected_result)

    def test_deep_find_with_nested_dicts_dfs(self):
        do_obj = DeepOps(self.nested_dicts)
        expected_result = {'a': 1,'b': {'a': 3}}
        self.assertEqual(do_obj.deep_find('a'), expected_result)

    def test_deep_find_with_simple_list_with_dict_dfs(self):
        do_obj = DeepOps(self.simple_list_with_dict)
        expected_result = 1
        self.assertEqual(do_obj.deep_find('a'), expected_result)

    def test_deep_find_with_nested_dicts_and_lists_dfs(self):
        do_obj = DeepOps(self.nested_dicts_and_lists)
        expected_result = [{'a' : 2}]
        self.assertEqual(do_obj.deep_find('b'), expected_result)

    # ------------------- deep_find_all DFS tests -------------------

    def test_deep_find_all_with_simple_dicts_dfs(self):
        do_obj = DeepOps(self.simple_dict)
        expected_result = [1]
        self.assertEqual(do_obj.deep_find_all('a'), expected_result)

    def test_deep_find_all_with_nested_dicts_dfs(self):
        do_obj = DeepOps(self.nested_dicts)
        expected_result = [{'a': 1,'b': {'a': 3}}, 1, 3]
        self.assertEqual(do_obj.deep_find_all('a'), expected_result)

    def test_deep_find_all_with_simple_list_with_dict_dfs(self):
        do_obj = DeepOps(self.simple_list_with_dict)
        expected_result = [1]
        self.assertEqual(do_obj.deep_find_all('a'), expected_result)

    def test_deep_find_all_with_nested_dicts_and_lists_dfs(self):
        do_obj = DeepOps(self.nested_dicts_and_lists)
        expected_result = [[{'a': 2}], [{'b': 2}], 2]
        self.assertEqual(do_obj.deep_find_all('b'), expected_result)

    # ----------------------- BFS TESTS --------------------------
    # -------------------- deep_find BFS tests -------------------

    def test_deep_find_with_simple_dict_bfs(self):
        do_obj = DeepOps(self.simple_dict)
        expected_result = 1
        self.assertEqual(do_obj.deep_find('a', bfs=True), expected_result)

    def test_deep_find_with_nested_dicts_bfs(self):
        do_obj = DeepOps(self.nested_dicts)
        expected_result = {'a': 1,'b': {'a': 3}}
        self.assertEqual(do_obj.deep_find('a', bfs=True), expected_result)

    def test_deep_find_with_simple_list_with_dict_bfs(self):
        do_obj = DeepOps(self.simple_list_with_dict)
        expected_result = 1
        self.assertEqual(do_obj.deep_find('a', bfs=True), expected_result)

    def test_deep_find_with_nested_dicts_and_lists_bfs(self):
        do_obj = DeepOps(self.nested_dicts_and_lists)
        expected_result = [{'a' : 2}]
        self.assertEqual(do_obj.deep_find('b', bfs=True), expected_result)

    # ------------------ deep_find_all BFS tests ------------------

    def test_deep_find_all_with_simple_dicts_bfs(self):
        do_obj = DeepOps(self.simple_dict)
        expected_result = [1]
        self.assertEqual(do_obj.deep_find_all('a', bfs=True), expected_result)

    def test_deep_find_all_with_nested_dicts_bfs(self):
        do_obj = DeepOps(self.nested_dicts)
        expected_result = [{'a': 1,'b': {'a': 3}}, 1, 3]
        self.assertEqual(do_obj.deep_find_all('a', bfs=True), expected_result)

    def test_deep_find_all_with_simple_list_with_dict_bfs(self):
        do_obj = DeepOps(self.simple_list_with_dict)
        expected_result = [1]
        self.assertEqual(do_obj.deep_find_all('a', bfs=True), expected_result)

    def test_deep_find_all_with_nested_dicts_and_lists_bfs(self):
        do_obj = DeepOps(self.nested_dicts_and_lists)
        expected_result = [[{'a': 2}], [{'b': 2}], 2]
        self.assertEqual(do_obj.deep_find_all('b', bfs=True), expected_result)

    # ------------------ OTHER DEEP_<METHOD> TESTS --------------------
    # -----------------------------------------------------------------
    # -------------------- deep_update tests --------------------------

    def test_deep_update_with_simple_dict_dfs(self):
        do_obj = DeepOps(self.simple_dict)
        do_obj.deep_update('a', 2)
        expected_result = {'a': 2, 'b': 2}
        self.assertEqual(self.simple_dict, expected_result)

    def test_deep_update_with_nested_dicts_dfs(self):
        do_obj = DeepOps(self.nested_dicts)
        do_obj.deep_update('b', 2)
        expected_result = {
            'a': {
                'a': 1,
                'b': 2
            },
            'b': 2
        }
        self.assertEqual(self.nested_dicts, expected_result)
    
    def test_deep_update_with_simple_list_with_dict_dfs(self):
        do_obj = DeepOps(self.simple_list_with_dict)
        do_obj.deep_update('b', 3)
        expected_result = [{'a': 1, 'b': 3}]
        self.assertEqual(self.simple_list_with_dict, expected_result)

    def test_deep_update_with_nested_dicts_and_lists_dfs(self):
        do_obj = DeepOps(self.nested_dicts_and_lists)
        do_obj.deep_update('b', 1)
        expected_result = [
            {
                'a': 1,
                'b': 1
            },
            {
                'b' : 1
            }
        ]
        self.assertEqual(self.nested_dicts_and_lists, expected_result)

    # -------------------- deep_compare tests --------------------------
    
    # ----------------------- simple dicts -----------------------------

    def test_deep_compare_when_both_simple_dicts_are_empty_return_true(self):
        d1 = {}
        d2 = {}
        do_obj = DeepOps(d1)
        self.assertTrue(do_obj.deep_compare(d2))
    
    def test_deep_compare_when_both_simple_dicts_are_equal_return_true(self):
        d1 = {'a': 1, 'b': 2}
        d2 = {'a': 1, 'b': 2}
        do_obj = DeepOps(d1)
        self.assertTrue(do_obj.deep_compare(d2))

    def test_deep_compare_when_one_of_the_simple_dicts_is_empty_return_false(self):
        d1 = {'a': 1, 'b': 2}
        d2 = {}  # empty dict
        do_obj = DeepOps(d1)
        self.assertFalse(do_obj.deep_compare(d2))

    def test_deep_compare_when_simple_dicts_have_different_keys_return_false(self):
        d1 = {'a': 1, 'b': 2}
        d2 = {'a1': 1, 'b': 2}  # different key
        do_obj = DeepOps(d1)
        self.assertFalse(do_obj.deep_compare(d2))
    
    def test_deep_compare_when_simple_dicts_have_different_values_return_false(self):
        d1 = {'a': 1, 'b': 2}
        d2 = {'a': 1, 'b': 1}  # differenet value
        do_obj = DeepOps(d1)
        self.assertFalse(do_obj.deep_compare(d2))

    def test_deep_compare_when_simple_dicts_have_different_values_and_keys_return_false(self):
        d1 = {'a1': 1, 'b': 1}  # differenet value and key
        d2 = {'a': 1, 'b': 1}  
        do_obj = DeepOps(d1)
        self.assertFalse(do_obj.deep_compare(d2))
    
    def test_deep_compare_when_simple_dicts_have_different_lengths_return_false(self):
        d1 = {'a': 1, 'b': 1, 'c': 1}  # extra key
        d2 = {'a': 1, 'b': 1}  
        do_obj = DeepOps(d1)
        self.assertFalse(do_obj.deep_compare(d2))

    # ----------------------- nested dicts -----------------------------

    def test_deep_compare_when_nested_dicts_are_equal_return_true(self):
        d1 = {'a': {
                'a1': 1,
                'a2': {'a21': 21}
            }}
        d2 = {'a': {
                'a1': 1,
                'a2': {'a21': 21}
            }} 
        do_obj = DeepOps(d1)
        self.assertTrue(do_obj.deep_compare(d2))

    def test_deep_compare_when_nested_dicts_have_different_keys_return_false(self):
        d1 = {'a': {
                'a1': 1,
                'a2': {'a21': 21}
            }}
        d2 = {'a': {
                'a1': 1,
                'a2': {'a22': 21}  # different key
            }} 
        do_obj = DeepOps(d1)
        self.assertFalse(do_obj.deep_compare(d2))

    def test_deep_compare_when_nested_dicts_have_different_values_return_false(self):
        d1 = {'a': {
                'a1': 1,
                'a2': {'a21': 21}
            }}
        d2 = {'a': {
                'a1': 1,
                'a2': {'a21': 22}  # different value
            }} 
        do_obj = DeepOps(d1)
        self.assertFalse(do_obj.deep_compare(d2))

    def test_deep_compare_when_nested_dicts_have_different_values_and_keys_return_false(self):
        d1 = {'a': {
                'a1': 1,
                'a2': {'a21': 21}
            }}
        d2 = {'a': {
                'a': 1, # different key
                'a2': {'a21': 22}  # different value
            }} 
        do_obj = DeepOps(d1)
        self.assertFalse(do_obj.deep_compare(d2))

    def test_deep_compare_when_nested_dicts_have_different_lengths_return_false(self):
        d1 = {'a': {
                'a1': 1,
                'a2': {'a21': 21}
            }}
        d2 = {'a': {
                'a1': 1,
                'a2': {'a21': 21,
                       'a22': 22}  # extra key
            }} 
        do_obj = DeepOps(d1)
        self.assertFalse(do_obj.deep_compare(d2))

    # ----------------------- lists with dicts -----------------------------

    def test_deep_compare_when_both_lists_w_dicts_are_empty_return_true(self):
        d1 = []
        d2 = []
        do_obj = DeepOps(d1)
        self.assertTrue(do_obj.deep_compare(d2))
    
    def test_deep_compare_when_both_lists_w_dicts_are_equal_return_true(self):
        d1 = [
            {'a': 1},
            {'b': [1, 2, 3]}
        ]
        d2 = [
            {'a': 1},
            {'b': [1, 2, 3]}
        ]
        do_obj = DeepOps(d1)
        self.assertTrue(do_obj.deep_compare(d2))

    def test_deep_compare_when_one_of_the_lists_w_dicts_is_empty_return_false(self):
        d1 = [{'a': 1, 'b': 2}]
        d2 = []  # empty list
        do_obj = DeepOps(d1)
        self.assertFalse(do_obj.deep_compare(d2))

    def test_deep_compare_when_lists_w_dicts_have_different_keys_return_false(self):
        d1 = [
            {'a1': 1},  # differenet key
            {'b': [1, 2, 3]}
        ]
        d2 = [
            {'a': 1},
            {'b': [1, 2, 3]}
        ]
        do_obj = DeepOps(d1)
        self.assertFalse(do_obj.deep_compare(d2))
    
    def test_deep_compare_when_lists_w_dicts_have_different_values_in_nested_list_return_false(self):
        d1 = [
            {'a': 1},  
            {'b': [1, 2, 3]}
        ]
        d2 = [
            {'a': 1},
            {'b': [1,2, 4]}  # different value
        ]
        do_obj = DeepOps(d1)
        self.assertFalse(do_obj.deep_compare(d2))

    def test_deep_compare_when_lists_w_dicts_have_different_values_and_keys_return_false(self):
        d1 = [
            {'a': 1},  
            {'b1': [1, 2, 3]}  # different key
        ]
        d2 = [
            {'a': 2},  # diffrenet value
            {'b': [1, 2, 3]}
        ]
        do_obj = DeepOps(d1)
        self.assertFalse(do_obj.deep_compare(d2))
    
    def test_deep_compare_when_lists_w_dicts_have_different_lengths_return_false(self):
        d1 = [
            {'a': 1},  
            {'b1': [1, 2, 3],
             'b2': 3}  # extra key
        ]
        d2 = [
            {'a': 2},
            {'b': [1, 2, 3]}
        ]  
        do_obj = DeepOps(d1)
        self.assertFalse(do_obj.deep_compare(d2))

    # ----------------------- more complex data ----------------------------
    
    def test_deep_compare_when_complex_data_has_different_types_return_false(self):
        d1 = {
            'a': (1, { 
                'a1': 1
            }),
            'b': {'b1': 1}
        }
        d2 = {
            'a': [1, {  # tuple instead of list
                'a1': 1
            }],
            'b': {'b1': 1}
        }
        do_obj = DeepOps(d1)
        self.assertFalse(do_obj.deep_compare(d2))

    # -------------------- schema_validator tests --------------------------

    def test_schema_validator_with_simple_dict_and_schema_of_different_lengths_return_true(self):
        schema = ['a', 'b', 'c']  # schema has extra key 'c'
        do_obj = DeepOps(self.simple_dict)
        self.assertFalse(do_obj.schema_validator(schema))

    def test_schema_validator_with_simple_dict_valid_to_schema_return_true(self):
        schema = ['a', 'b']
        do_obj = DeepOps(self.simple_dict)
        self.assertTrue(do_obj.schema_validator(schema))
    
    def test_schema_validator_with_simple_dict_invalid_to_schema_return_false(self):
        schema = ['a', 'c']  # second key of simple_dict is 'b'
        do_obj = DeepOps(self.simple_dict)
        self.assertFalse(do_obj.schema_validator(schema))

    def test_schema_validator_with_nested_dicts_valid_to_schema_return_true(self):
        schema = [
            ['a', [
                'a', 
                ['b', ['a']]
            ]],
            ['b', [
                'b'
            ]]
        ]
        do_obj = DeepOps(self.nested_dicts)
        self.assertTrue(do_obj.schema_validator(schema))
    
    def test_schema_validator_with_nested_dicts_ininvalid_to_schema_return_false(self):
        schema = [
            ['a', [
                'a', 
                ['b', ['a1']]  # key 'a1' in nested dicts is 'a'
            ]],
            ['b', [
                'b'
            ]]
        ]
        do_obj = DeepOps(self.nested_dicts)
        self.assertFalse(do_obj.schema_validator(schema))

if __name__ == "__main__":
    unittest.main()
