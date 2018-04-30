"""
TODO
- official comment format
- make your code beautiful and easy to read
"""

"""
Guarantees:
- Input file will only contain: "X", " ", "O", and newlines
- Length of each row will be equal
- Length of each column will be equal
- Size will be less than 250x250
"""
from sys import argv


def main(argv):
    blob_elements = ["X", "O"]

    #open input file containing matrix to find blobs in
    test_file = open(argv[1], "r")

    #move into 2D list of characters
    array = parse_blob_file(test_file)
    test_file.close()
    
    #find max blob sizes for blob_elements and store in result
    result = {}
    for element in blob_elements:
        result[element] = find_max_blob(array, element)

    print(result)

        
def parse_blob_file(test_file):
    array = []
    for line in test_file:
        #strip guaranteed newline
        line = line[:len(line)-1]
        #split by spaces
        array.append(line.split(" "))

    #convert to 2d array of dicts whose value contains a "visited" element
    for row in range(len(array)):
        for col in range(len(array[0])):
            array[row][col] = { array[row][col] : 0 }
    
    return array


"""
Finds maximum blob size of "val" within an array
Returns max blob size as an int

OPTIMIZATION:
I think this could be more time efficient if text values in
the array were  replaced with objects whose values included
a "visited" element
"""
def find_max_blob(array, val):
    max_blob_size = 0
    for row in range(len(array)):
        for col in range(len(array[0])):
            if val in array[row][col] and array[row][col][val] == 0:
                cur_blob_size = blob_counter(array, val, row, col, 1)
                if cur_blob_size > max_blob_size:
                    max_blob_size = cur_blob_size
    return max_blob_size


def blob_counter(array, val, row, col, blob_size):
    #visit current
    array[row][col][val] = 1
    
    #check right (border? matching value? visited?)
    if col < len(array[0])-1:
        if (val in array[row][col+1]) and (array[row][col+1][val] == 0):
            blob_size += 1
            blob_counter(array, val, row, col+1, blob_size)
            
    #check down
    if row < len(array)-1:
        if (val in array[row+1][col]) and (array[row+1][col][val] == 0):
            blob_size += 1
            blob_counter(array, val, row+1, col, blob_size)
            
    #check left
    if col > 0:
        if (val in array[row][col-1]) and (array[row][col-1][val] == 0):
            blob_size += 1
            blob_counter(array, val, row, col-1, blob_size)
            
    #check up
    if row > 0:
        if (val in array[row-1][col]) and (array[row-1][col][val] == 0):
            blob_size += 1
            blob_counter(array, val, row-1, col, blob_size)

    return blob_size


if __name__ == "__main__":
    main(argv)
