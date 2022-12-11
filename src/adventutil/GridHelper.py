def get_numeric_grid(input, separator=None):
    """Generate a 2D array of integers.  If separator is None (default), every digit is considered a different element

        '' separator example                    ' ' separator example
        "12345"    [[1,2,3,4,5],                "12 3 45"      [[12, 3, 45],
        "67890" ->  [6,7,8,9,0],                "6 7 8 9 0" ->  [6, 7, 8, 9, 0],
        "11111"     [1,1,1,1,1]]                "11111"         [11111]]
    """
    grid = []
    for line in input:
        if not line:
            grid.append([])
            continue

        if separator != None:
            line = line.split(separator) 
        row = [int(i) for i in line]

        grid.append(row)

    return grid

def get_string_grid(input, separator=None):
    """Generate a 2D array of string.  If separator is None (default), every character is considered a different element
    """
    grid = []
    for line in input:
        if not line:
            grid.append([])
            continue

        row = list(line) if separator is None else line.split(separator)        
        grid.append(row)

    return grid

def __test():
    input = ["12345","67890","11111"]
    expected = [[1,2,3,4,5],[6,7,8,9,0],[1,1,1,1,1]]
    actual = get_numeric_grid(input)
    print("Test 1 result = {b}".format(b=expected==actual))

    input = ["12 3 45","6 7 8 9 0","11111"]
    expected = [[12,3,45],[6,7,8,9,0],[11111]]
    actual = get_numeric_grid(input,' ')
    print("Test 2 result = {b}".format(b=expected==actual))

    input = ["","6 7 8 9 0","11111"]
    expected = [[],[6,7,8,9,0],[11111]]
    actual = get_numeric_grid(input,' ')
    print("Test 3 result = {b}".format(b=expected==actual))

    input = ["abc","def","ghi"]
    expected = [['a','b','c'],['d','e','f'],['g','h','i']]
    actual = get_string_grid(input)
    print("Test 4 result = {b}".format(b=expected==actual))

    input = ["The;Final;Test","","The;End"]
    expected = [['The','Final','Test'],[],['The','End']]
    actual = get_string_grid(input,';')
    print("Test 5 result = {b}".format(b=expected==actual))

    
    

if __name__ == "__main__":
    __test()
