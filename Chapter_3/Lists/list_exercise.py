if __name__ == '__main__':
    x = [5, 7, 8, 1, 2]
    y = []
    for num in x:
        num **= 2
        y.append(num)
    y.sort(reverse=True)
    print(y)