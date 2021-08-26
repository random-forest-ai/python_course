if __name__ == '__main__':
    # def fun():
    #     print("This is my function.")
    # fun()

    # Inner function
    # def outer():
    #     def inner():
    #         print("This is inner function.")
    #     print("This is outer function.")
    #     inner()
    # outer()

    # Scope
    # def outer():
    #     def inner():
    #         print(x)
    #     x = 200
    #     inner()
    # x = 100
    # outer()

    # Out of Scope
    # def outer():
    #     x = 100
    # outer()
    # print(x)

    # Global Keyword
    def outer():
        global x
        print(x)
        x = x + 1
    x = 100
    outer()
    print(x)
