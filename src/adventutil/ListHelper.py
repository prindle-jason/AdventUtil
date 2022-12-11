def list_split(list, delimiter):
    """Split a list in sublists separated on delimiter element
       Example:    split([1,2,0,0,5,0,1,3],0) -> [[1,2],[],[5],[1,3]]
    """
    result = []
    sublist = []
    for x in list:
        if x == delimiter:
            result.append(sublist.copy())
            sublist.clear()
            continue
        sublist.append(x)
    
    result.append(sublist)
    return result

def list_strip(list):
    return [e.strip() for e in list]

def __test():
    split_input = [1,2,0,0,5,0,1,3]
    split_delimiter = 0
    split_expected = [[1,2],[],[5],[1,3]]

    split_actual = list_split(split_input, split_delimiter)
    print(split_actual == split_expected)
    #print(split_actual)
    #print(split_expected)
    

if __name__ == "__main__":
    __test()
