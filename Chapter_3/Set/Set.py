if __name__ == '__main__':
    # Declare

    # x = set()
    # x = {1}
    # x = {1, 2, 3, "Apple", True, 4.0, (1, 2, 3)}

    x = {1, 2, 3, 1}
    # Mutable type: List, Set
    # x = {{1, 2}, {3, 4}} # Not OK
    # x = {(1,2), ['a', 'b', 'c']} # Not OK

    # Add
    # x = {'I', 'love', 'apple'}
    # x.add('You')

    # Remove
    # x.remove('apple')
    # y = x.pop()
    # print(y)

    # Set Operation

    print("Apple" in {"Hong Kong", "Taiwan"})
    print(3 not in {3, 7, 9})

    A = {1, 3, 5, 6, 8}
    B = {1, 2, 4, 7, 5}

    print(A | B)
    print(A & B)
    print(A - B)
    print(A ^ B)