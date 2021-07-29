if __name__ == '__main__':
    # Exercise1
    # m, n = 4, 3

    # Method 1
    # result = []
    # for i in range(m):
    #     row = []
    #     for j in range(n):
    #         row.append(i * j)
    #     result.append(row)

    # Method 2
    # result = [[i * j for j in range(n)] for i in range(m)]
    #
    # for row in result:
    #     print(*row)


    # Exercise 2
    # m, n = 10, 10

    # Method 1
    # result = []
    # for i in range(m):
    #     row = []
    #     for j in range(n):
    #         if (i + j) % 2 == 0: # % precedence is higher than +
    #             row.append('O')
    #         else:
    #             row.append('X')
    #     result.append(row)

    # result = [['O' if (i + j) % 2 == 0 else 'X' for j in range(n)] for i in range(m)]
    # for row in result:
    #     print(*row)

    # Exercise 3
    # fib = [0, 1]
    # while fib[-1] + fib[-2] < 100:
    #     fib.append(fib[-1] + fib[-2])
    # print(*fib, sep=", ")

    # Exercise 4
    # Method 1: String method
    string = 'racecar'
    # print(list(reversed(string)) == list(string))

    # Method 2 (For loop)
    # result = True
    # for i in range(0, len(string) // 2):
    #     if string[i] != string[-i - 1]:
    #         result = False
    #         break
    # print(result)

    # Method 3 (List Comprehension)
    result = [string[i] == string[-i - 1] for i in range(0, len(string) // 2)]
    print(all(result))