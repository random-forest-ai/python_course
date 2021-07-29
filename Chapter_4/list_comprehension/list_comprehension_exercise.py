if __name__ == '__main__':
    # Exercise1
    # x = [5,7,8,1,2]
    # y = [num ** 2 for num in x]
    # y.sort(reverse=True)
    # print(y)

    # Exercise2
    # distance_from_HK = {"London": 9623, "New York": 12947,
    #                     "Lima": 18439, "Singapore": 2587,
    #                     "Vienna": 8729, "Londres": 9623,
    #                     "Wien": 8729, "Istanbul": 8017}
    # y = {city: distance * 0.621 for city, distance in distance_from_HK.items()}
    # print(y)

    # Exercise3
    num = 10
    y = ['*' * i for i in range(1, num)] + ['*' * i for i in range(num, 0, -1)]
    for line in y:
        print(*line)