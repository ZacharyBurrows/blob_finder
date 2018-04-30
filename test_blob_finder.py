#test file
import unittest
import blob_finder

class TestBlobFinder(unittest.TestCase):
    
    def test_find_max_blob(self):
        test_array = [['X','X','X'],
                      ['X','X','X'],
                      ['X','X','X']]
        
        self.assertEqual(main.find_max_blob(test_array), 9)


if __name__ == '__main__':
    unittest.main()










"""
    Test Cases:
     1) File doesn't exist
     2) File is invalid format
         ~ contains values other than X or O), has wrong number or rows/columns
     3) 
"""
