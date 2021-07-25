if __name__ == '__main__':
    # == / != / < / <= / > / >= operator (Change the operator as you wish!)
    # print(7 == 7)
    # print(7 == 8)
    # print(7 == 7.0)
    # print("ABC" == "ABC")
    # print("ABC" == "ABCD")
    # print("ABC" == "abc")
    # print((5, 3, 2) == (5, 3, 2))
    # print((5, 3, 2) == (5, 3, 2.1))

    # = vs ==
    x = 2
    print(x == 2)

    # Logic Relation

    # not
    print(not 7 >= 7)

    # and
    print(7 >= 7 and "Apple" > "Banana")

    # short circuit
    print(False and 3 / 0) # OK
    print(True and 3 / 0)  # Error

    # or
    print(7 >= 7 or "Apple" > "Banana")

    # short circuit
    print(True or 3 / 0)  # OK
    print(False or 3 / 0)  # Error
