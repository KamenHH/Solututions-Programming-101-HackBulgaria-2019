import unittest
from unittest.mock import patch
import keys


class KeysTestCase(unittest.TestCase):
    ex1 = [('f', 1), ('g', 2), ('f', 3), ('h', 10), ('f', 5), ('h', 2)]
    ex2 = [('c', 1), ('b', 2), ('a', 2), ('d', 3)]

    def test_get_input_ex1(self):
        with patch('keys.get_input') as mocked_input:
            mocked_input.return_value = self.ex1
            result = keys.get_input()
            self.assertEqual(result, [('f', 1), ('g', 2), ('f', 3),
                                      ('h', 10), ('f', 5), ('h', 2)])

    def test_get_input_ex2(self):
        with patch('keys.get_input') as mocked_input:
            mocked_input.return_value = self.ex2
            result = keys.get_input()
            self.assertEqual(result, [('c', 1), ('b', 2), ('a', 2), ('d', 3)])

    def test_reduce_ex1(self):
        result = keys.reduce(self.ex1)
        self.assertEqual(result, {'f': 9, 'g': 2, 'h': 12})

    def test_reduce_ex2(self):
        result = keys.reduce(self.ex2)
        self.assertEqual(result, {'a': 2, 'b': 2, 'c': 1, 'd': 3})

    def test_get_top3_ex1(self):
        data = {'f': 9, 'g': 2, 'h': 12}
        result = keys.get_top3(data)
        self.assertEqual(result, [('h', 12), ('f', 9), ('g', 2)])

    def test_get_top3_ex2(self):
        data = {'a': 2, 'b': 2, 'c': 1, 'd': 3}
        result = keys.get_top3(data)
        self.assertEqual(result, [('d', 3), ('a', 2), ('b', 2)])


if __name__ == '__main__':
    unittest.main()
