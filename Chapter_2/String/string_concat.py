if __name__ == '__main__':
    # str = "Apple" + "Orange" # + operation both side String
    # print(str)
    # str = "Apple" + str(42) # str(42) is now string type
    # print(str)

    # Method 2: format()
    # str = "Apple {}"
    # print(str.format("Orange")) # Orange will go to {}

    str = "Apple {} {}"
    print(str.format("Orange", "Banana"))  # Orange will go to 1st {}, Banana 2nd