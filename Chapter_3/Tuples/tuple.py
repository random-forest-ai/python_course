if __name__ == '__main__':
    # Creating a tuple
    x = ()

    x = (1, )
    print(type(x))

    x = (1)
    print(type(x))

    x = (1, 2, 3, "Apple", True, 4.0)

    x = ((1, 2, 3), (4, 5, 6))

    #Accessing Tuple
    x = (1, 2, 3, "Apple", True, (7, 7, 7), 4.0)

    print(x[3])
    print(x[-2])
    print(x[1:2])
    print(x[1:3])
    print(x[::2])

    _, _, _, _, _, _, x7 = x
    print(x7)

    print(x[5][1])

    # Modify tuple
    x[0] = 2
    x = (1, 2, 3)

    # Tuple Operation
    print((1, 2) + (3, 4, 5))
    print((1, 2) * 3)
    print(len(1, 2, 3))
    print("Apple" in ("Hong Kong", "Taiwan"))
    print(4 not in (3, 7, 9))

    x = (1,2,3,1)
    print(x.count(1))
    print(x.index(1))

    for num in x:
        print(num, end=" ")