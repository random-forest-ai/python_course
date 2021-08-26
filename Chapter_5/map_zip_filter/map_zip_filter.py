if __name__ == '__main__':
    # Map
    def double(num):
        return num + num
    y = map(double, [1,2,3,4])
    print(list(y))

    list(map(lambda num: num + num, [1, 2, 3, 4]))
    list(map(lambda x, y: x * y, [1, 2, 3, 4], [5, 6, 7, 8]))

    # Filter
    def is_even(number):
        return number % 2 == 0

    list(filter(is_even, range(10)))

    def long_word(string):
        return len(string) >= 5

    words = {'Harry', 'Potter', 'Me', 'United States', 'Innsbruck'}
    list(filter(long_word, words))

    list(filter(lambda string: len(string) >= 5, words))

    # Zip
    list(zip((1, 3, 5), (2, 4, 6)))
    list(zip(range(10), (2, 4, 6)))

    list(zip((1, 3, 5), (2, 4, 6), (10, 20, 30)))

    info = [('name', 'age', 'GPA', 'Gender'), ('Ben', 25, 4.0, 'Unknown')]
    list(zip(*info))

    list(zip(('name', 'age', 'GPA', 'Gender'), ('Ben', 25, 4.0, 'Unknown')))

    # Sorted
    numbers = [-9, 3, 7, 8]
    sorted(numbers)

    # Define own sorting function
    def squares(num):
        return num ** 2

    sorted(numbers, key=squares)
    sorted(numbers, key=lambda num: num ** 2)