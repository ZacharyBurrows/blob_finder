import unittest
import blob_finder
import os
import tempfile

"""
TEST#2

"""

class TestBlobFinder(unittest.TestCase):
    """
    TEST#1
    a) Write sample data to a temporary file
    b) Parse with the parse_blob_file function
    c) Call find_blobs on the data and test the result for expected output.
    """
    def test_blob_counter(self):
        with tempfile.TemporaryFile('w+') as tmp:
            tmp.write("X X X X\n"
                      "X O O X\n"
                      "X O O X\n"
                      "X X X X\n")
                
            tmp.seek(0)
            blob_2D = blob_finder.parse_blob_file(tmp)
            blob_size = blob_finder.blob_counter(blob_2D, "O", 1, 1, 0)
            self.assertEqual(blob_size, 4)

            tmp.seek(0)
            blob_size = blob_finder.blob_counter(blob_2D, "X", 0, 0, 0)
            self.assertEqual(blob_size, 12)

        with tempfile.TemporaryFile('w+') as tmp:
            tmp.write("X X O O\n"
                      "O X O O\n"
                      "O X X O\n"
                      "O O X X\n")
                
            tmp.seek(0)
            blob_2D = blob_finder.parse_blob_file(tmp)
            blob_size = blob_finder.blob_counter(blob_2D, "X", 3, 3, 0)
            self.assertEqual(blob_size, 7)

            tmp.seek(0)
            blob_size = blob_finder.blob_counter(blob_2D, "O", 3, 0, 0)
            self.assertEqual(blob_size, 4)

    def test_find_max_blob(self):
        with tempfile.TemporaryFile('w+') as tmp:
            tmp.write("X X X X\n"
                      "X O O X\n"
                      "X O O X\n"
                      "X X X X\n")
                
            tmp.seek(0)
            blob_2D = blob_finder.parse_blob_file(tmp)
            max_blob_size = blob_finder.find_max_blob(blob_2D, "O")
            self.assertEqual(max_blob_size, 4)

            tmp.seek(0)
            blob_2D = blob_finder.parse_blob_file(tmp)
            max_blob_size = blob_finder.find_max_blob(blob_2D, "X")
            self.assertEqual(max_blob_size, 12)

            with tempfile.TemporaryFile('w+') as tmp:
                tmp.write("X X X X X X X X X X\n"
                          "X X X X X X X X X X\n"
                          "X X X X X X X X X X\n"
                          "X X X X X X X X X X\n"
                          "X X X X X X X X X X\n"
                          "X X X X X X X X X X\n"
                          "X X X X X X X X X X\n"
                          "X X X X X X X X X X\n"
                          "X X X X X X X X X X\n"
                          "X X X X X X X X X X\n"
                          "X X X X X X X X X X\n"
                          "X X X X X X X X X X\n"
                          "X X X X X X X X X X\n"
                          "X X X X X X X X X X\n"
                          "X X X X X X X X X X\n"
                          "X X X X X X X X X X\n"
                          "X X X X X X X X X X\n"
                          "X X X X X X X X X X\n"
                          "X X X X X X X X X X\n"
                          "X X X X X X X X X O\n")
                
                tmp.seek(0)
                blob_2D = blob_finder.parse_blob_file(tmp)
                max_blob_size = blob_finder.find_max_blob(blob_2D, "O")
                self.assertEqual(max_blob_size, 1)

                tmp.seek(0)
                blob_2D = blob_finder.parse_blob_file(tmp)
                max_blob_size = blob_finder.find_max_blob(blob_2D, "X")
                self.assertEqual(max_blob_size, 199)
    
    

if __name__ == '__main__':
    unittest.main() 
