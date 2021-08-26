if __name__ == '__main__':
    # Exercise 1

    # not_contains_vowel('Apple') --> False
    # not_contains_vowel('Sync') --> True
    # def not_contains_vowel(string):
    #     vowels = {'a', 'e', 'i', 'o', 'u'}
    #     return not any([char in vowels for char in string.lower()])
    #
    # # Input: ['Apple', 'Sync', 'Not', 'Rhythm', 'Difficult', 'Psst']
    # # Output: ['Sync', 'Rhythm', 'Psst']
    # def no_vowel_words(strings):
    #     return filter(not_contains_vowel, strings)
    #
    # print(list(no_vowel_words(['Apple', 'Sync', 'Not', 'Rhythm', 'Difficult', 'Psst'])))

    # Exercise 2
    def pairing(num):
        return list(zip(range(num + 1), range(num, -1, -1)))
        # return [(n, num - n) for n in range(num + 1)]

    print(pairing(5))