import sys

if __name__ == '__main__':
    age = input("Please enter your current age ")
    print("Your current age is {}".format(age))
    print("You will be {} years old 10 years later".format(int(age) + 10))
    
    # Writing Mode
    # file = open('random.txt', 'w')
    # file.write('I love Apple')

    # Append mode
    # file = open('random.txt', 'a')
    # file.write('I really love Apple.')

    # file = open('a_tale_of_two_cities.txt', 'r')
    # content = file.read()
    # print(content)

    # args = sys.argv[1:]
    # print("Hi {}! Your current age is {}".format(args[0], args[1]))



