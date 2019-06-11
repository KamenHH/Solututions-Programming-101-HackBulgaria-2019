import unittest
from unittest.mock import patch
import intervals


class IntervalsTest(unittest.TestCase):
    ex1 = [-181, -414, 441, 889, -547, -313, 622, 679, 782, -640]
    ex2 = [123, 567, 124, 568, -100, -99]

    def test_get_input_ex1(self):
        with patch('intervals.get_input') as mocked_get_input:
            mocked_get_input.return_value = self.ex1
            result = intervals.get_input()
            self.assertEqual(result, [-181, -414, 441, 889, -547,
                                      -313, 622, 679, 782, -640])

    def test_get_input_ex2(self):
        with patch('intervals.get_input') as mocked_get_input:
            mocked_get_input.return_value = self.ex2
            result = intervals.get_input()
            self.assertEqual(result, [123, 567, 124, 568, -100, -99])

    def test_sort_data_ex1(self):
        result = intervals.sort_data(self.ex1)
        self.assertEqual(result, [-640, -547, -414, -313, -181, 441, 622, 679, 782, 889])

    def test_sort_data_ex2(self):
        result = intervals.sort_data(self.ex2)
        self.assertEqual(result, [-100, -99, 123, 124, 567, 568])

    def test_build_intervals_ex1(self):
        result = intervals.build_intervals(self.ex1)
        self.assertEqual(result, [(-181, -181, 1), (-414, -414, 1),
                                  (441, 441, 1), (889, 889, 1),
                                  (-547, -547, 1), (-313, -313, 1),
                                  (622, 622, 1), (679, 679, 1),
                                  (782, 782, 1), (-640, -640, 1)])

    def test_build_intervals_ex2(self):
        result = intervals.build_intervals(self.ex2)
        self.assertEqual(result, [(123, 123, 1), (567, 567, 1),
                                  (124, 124, 1), (568, 568, 1),
                                  (-100, -99, 2)])


if __name__ == '__main__':
    unittest.main()
