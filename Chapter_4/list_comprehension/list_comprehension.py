if __name__ == '__main__':
    x = [1,2,3,4]

    # Same

    # y = [num ** 2 for num in x]
    # print(y)
    #
    # y = []
    # for num in x:
    #     y.append(num ** 2)
    # print(y)

    # Same

    # y = [num ** 2 for num in x if num % 2 == 0]
    # print(y)
    #
    # y = []
    # for num in x:
    #     if num % 2 == 0:
    #         y.append(num ** 2)
    # print(y)

    # Same

    # y = [num ** 3 if num % 2 == 0 else num ** 2 for num in x]
    # print(y)
    #
    # y = []
    # for num in x:
    #     if num % 2 == 0:
    #         y.append(num ** 3)
    #     else:
    #         y.append(num ** 2)
    # print(y)

    # Same

    # x = ["Apple", "Banana", "Citrus", "A longggggg String"]
    #
    # y = [length for str in x if (length := len(str))  >= 6]
    # print(y)
    #
    # y = []
    # for str in x:
    #     if (length := len(str))  >= 6:
    #         y.append(length)
    # print(y)

    # Same

    # y = [(i, j) for i in range(3) for j in range(i, 3)]
    # print(y)
    #
    # y = []
    # for i in range(3):
    #     for j in range(i, 3):
    #         y.append((i, j))
    # print(y)