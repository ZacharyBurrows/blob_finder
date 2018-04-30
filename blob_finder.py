from sys import argv


def main(argv):
    blob_elements = ["X", "O"]

    #open input file containing matrix to find blobs in
    test_file = open(argv[1], "r")

    #move into 2D list of characters
    blob_2D = parse_blob_file(test_file)
    test_file.close()
    
    #find max blob sizes for blob_elements and store in result
    result = {}
    for element in blob_elements:
        result[element] = find_max_blob(blob_2D, element)

    print(result)


def parse_blob_file(test_file):
    blob_2D = []
    for line in test_file:
        #strip guaranteed newline
        line = line[:len(line)-1]
        #split by spaces
        blob_2D.append(line.split(" "))

    #convert to 2d array of dicts whose value contains a "visited" element
    for row in range(len(blob_2D)):
        for col in range(len(blob_2D[0])):
            blob_2D[row][col] = { blob_2D[row][col] : 0 }
    
    return blob_2D


"""
FUNCTION:
Finds maximum blob size of "val" within an array
Returns max blob size as an int

OPTIMIZATION:
I've replaced text values in the array with dicts whose keys
are the text, and value is a "visited" element
"""
def find_max_blob(blob_2D, val):
    max_blob_size = 0
    for row in range(len(blob_2D)):
        for col in range(len(blob_2D[0])):
            if val in blob_2D[row][col] and blob_2D[row][col][val] == 0:
                cur_blob_size = blob_counter(blob_2D, val, row, col, 0)
                if cur_blob_size > max_blob_size:
                    max_blob_size = cur_blob_size
    return max_blob_size


def blob_counter(blob_2D, val, row, col, blob_size):
    #"visit" current element and increment blob_size
    blob_2D[row][col][val] = 1
    blob_size += 1
    
    #check right (border? matching value? visited?)
    if col < len(blob_2D[0])-1:
        if (val in blob_2D[row][col+1]) and (blob_2D[row][col+1][val] == 0):
            blob_size = blob_counter(blob_2D, val, row, col+1, blob_size)
            
    #check down
    if row < len(blob_2D)-1:
        if (val in blob_2D[row+1][col]) and (blob_2D[row+1][col][val] == 0):
            blob_size = blob_counter(blob_2D, val, row+1, col, blob_size)
            
    #check left
    if col > 0:
        if (val in blob_2D[row][col-1]) and (blob_2D[row][col-1][val] == 0):
            blob_size = blob_counter(blob_2D, val, row, col-1, blob_size)
            
    #check up
    if row > 0:
        if (val in blob_2D[row-1][col]) and (blob_2D[row-1][col][val] == 0):
            blob_size = blob_counter(blob_2D, val, row-1, col, blob_size)

    return blob_size


if __name__ == "__main__":
    main(argv)
