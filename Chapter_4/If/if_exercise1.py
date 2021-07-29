if __name__ == '__main__':
    num = 10
    # if num % 2 == 0: # Divisible by 2?
    #     print("The number is divisible by 2.")
    # elif num % 3 == 0:
    #     print("The number is divisible by 3.")
    # elif num % 2 == 0 and num % 3 == 0:
    #     print("The number is divisible by 2 and 3.")
    # else:
    #     print("The number is neither divisible by 2 nor 3.")

    # if num % 2 == 0 and num % 3 != 0:  # Divisible by 2?
    #     print("The number is divisible by 2.")
    # elif num % 3 == 0 and num % 2 != 0:
    #     print("The number is divisible by 3.")
    # elif num % 2 == 0 and num % 3 == 0:
    #     print("The number is divisible by 2 and 3.")
    # else:
    #     print("The number is neither divisible by 2 nor 3.")

    # if num % 2 == 0 and num % 3 == 0:
    #     print("The number is divisible by 2 and 3.")
    # elif num % 2 == 0:  # Divisible by 2?
    #     print("The number is divisible by 2.")
    # elif num % 3 == 0:
    #     print("The number is divisible by 3.")
    # else:
    #     print("The number is neither divisible by 2 nor 3.")

    if num % 2 == 0:
        if num % 3 == 0:
            print("The number is divisible by 2 and 3.")
        else:
            print("The number is divisible by 2.")
    else:
        if num % 3 == 0:
            print("The number is divisible by 3.")
        else:
            print("The number is neither divisible by 2 nor 3.")