if __name__ == '__main__':
    string = "Apple"
    tuple = (1, 2, 5, 7)
    list = ['Andrew', 'Ben', 'Carsten']
    dict = {"London": 9623, "New York": 12947, "Budapest": 8659}
    set = {1, 3, 5}

    for char in string:
        print(char, end = " ")

    sum(tuple)
    sum(set)
    max(list)
    min(list)

    any([0, False, 1])
    any([0, False])

    all([0, False, 1])
    all([1, True])

    # Iterable function
    x = [3, 7, 1]
    y = sorted(x)

    # List Method
    x.sort()

    y = sorted(x)
    y = sorted(x, key=x.get)
