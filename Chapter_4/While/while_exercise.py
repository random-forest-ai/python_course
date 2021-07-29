if __name__ == '__main__':
    num = 27
    print(num, end=" ")
    while num != 1:
        if num % 2 == 0: # Number is even
            num //= 2
        else:
            num = num * 3 + 1
        print(num, end=" ")
