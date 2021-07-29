if __name__ == '__main__':
    num = 10
    for i in range(1, num):
        for j in range(i):
            print("*", end=" ")
        print()

    for i in range(num, 0, -1):
        for j in range(i):
            print("*", end=" ")
        print()
    '''
    n = 4
    *
    **
    ***
    
    ****
    ***
    **
    *
    '''