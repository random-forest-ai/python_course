if __name__ == '__main__':
    # Exercise 1
    # fib(1) = 0
    # fib(2) = 1
    # fib(3) = 1
    # fib(4) = 2

    # def fib(n):
    #     if n == 1:
    #         return 0
    #     elif n == 2:
    #         return 1
    #     else:
    #         return fib(n - 1) + fib(n - 2)
    # print(fib(5))

    # Exercise 2
    # squares(4) --> [1, 4, 9, 16]
    def squares(n):
        if n == 0:
            return []
        else:
            result = squares(n - 1) # squares(3) --> [1, 4, 9]
            result.append(n ** 2)
            return result

    print(squares(4))