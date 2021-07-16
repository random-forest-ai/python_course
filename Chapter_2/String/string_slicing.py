if __name__ == '__main__':
    str = "Pineapple"
    '''
         index
    P    0
    i    1
    n    2
    e    3
    a    4
    p    5
    p    6  -3
    l    7  -2
    e    8  -1
    '''
    print(str[2]) # Get index 2 character
    print(str[-1])  # Get index -1 character
    print(str[1:3]) # Include index 1 exclude index 3
    print(str[:4]) # str[0:4]
    print(str[:-1]) # str[0:-1]
    print(str[5:]) # str[5: len(str) + 1]
    print(str[5:8:2]) # index 5 -> 7
    print(str[:8:2])  # index 0 -> 2 -> 4 -> 6