if __name__ == '__main__':
    list = [1, 3, 8, 199, 831, 128]
    count_even, count_odd = 0, 0
    for element in list:
        if element % 2 == 0: #Even
            count_even += 1
        else:
            count_odd += 1
    print("Counts for even number is: {}".format(count_even))
    print("Counts for odd number is: {}".format(count_odd))