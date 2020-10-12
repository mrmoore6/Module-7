import unittest
from fun_with_collections import  sort_and_search_array

class MyTestCase(unittest.TestCase):
    def test_array_search(self):
        test_Array = [1,7,4,6,5]
        self.assertEqual(2, sort_and_search_array.search_array(test_Array)) #inputed 4 to return 2 index
    def test_array_sort(self):
        test_Array = [6,5,4,3,2,1]
        expect_Array = [1,2,3,4,5,6]
        self.assertListEqual(expect_Array, sort_and_search_array.sort_array(test_Array),)



if __name__ == '__main__':
    unittest.main()
#test
