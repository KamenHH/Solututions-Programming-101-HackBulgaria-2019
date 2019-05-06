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

    def test_deep_update_simple_dict_dfs(self):
        do_obj = DeepOps(self.simple_dict)
        do_obj.deep_update('a', 2)
        expected_result = {'a': 2, 'b': 2}
        self.assertEqual(self.simple_dict, expected_result)

    def test_deep_update_nested_dicts_dfs(self):
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
    
    def test_deep_update_simple_list_with_dict_dfs(self):
        do_obj = DeepOps(self.simple_list_with_dict)
        do_obj.deep_update('b', 3)
        expected_result = [{'a': 1, 'b': 3}]
        self.assertEqual(self.simple_list_with_dict, expected_result)

    def test_deep_update_nested_dicts_and_lists_dfs(self):
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
    
    
if __name__ == "__main__":
    unittest.main()