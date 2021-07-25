if __name__ == '__main__':
    x = ['I', 'love', 'apple']

    # Append
    x.append('today')
    print(x)

    # Insert
    x.insert(2, 'many')
    print(x)

    # Extend
    x.extend(['and', 'tomorrow'])
    print(x)

    # Modify
    x[0] = 'You'
    x[4:7] = ['forever', 'and', 'forever']
    print(x)

    # Delete
    x.remove('apple')

    e = x.pop(0)
    print(e)
    print(x)

    del x[0]
    del x[0:2]
    del x

    # Methods

    x = [1,2,3,1]

    x.reverse()
    print(x)

    x.sort()
    print(x)

    x.sort(reverse=True)
    print(x)