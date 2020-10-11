import unittest
from unittest.mock import patch
from fun_with_collections import basic_list


class TestList(unittest.TestCase):
    @patch('fun_with_collections.basic_list.get_input', return_value='15')
    def test_make_list(self, input):
        self.assertEqual(basic_list.make_list(), [15, 15, 15])

if __name__ == '__main__':
    unittest.main()
