if __name__ == '__main__':
    # Arbitrary Number of Arguments
    # def greetings(*args):
    #     print(args)
    #     for name in args:
    #         print("Hi {}! How are you?".format(name))
    # greetings("Alan Turing", "Ada Lovelace", "Haskell Curry", "Alonzo Church")

    # Arbitrary Number of Key Arguments
    def greetings(**kwargs):
        print(kwargs)
        print("Hi {} {}! How are you?".format(kwargs['lastname'], kwargs['firstname']))
    greetings(lastname='Alan', firstname='Turing', field='Mathematics')

    # Mutable
    # def bar(list):
    #     list.append(100)
    #     print("Done")
    # x = [1]
    # bar(x)
    # print(x)

    # Immutable
    # def foo(val):
    #     val = val + 1
    #     print("Done")
    # x = 10
    # foo(x)
    # print(x)

    # Optional Parameter
    # def greetings(firstname, lastname, middlename=None):
    #     if middlename:
    #         print("Hi {} {} {}! How are you?".format(firstname, middlename, lastname))
    #     else:
    #         print("Hi {} {}! How are you?".format(firstname, lastname))
    # greetings('Ada', 'Lovelace', 'King')
    # greetings('Alan', 'Turing')

    # Positional Arguments + Keyword Arguments
    # def greetings(firstname, middlename, lastname):
    #     print("Hi {} {} {}! How are you?".format(firstname, middlename, lastname))
    # greetings('Ada', lastname='Lovelace', middlename='King')
    # greetings(lastname='Lovelace', middlename='King', 'Ada') #Error


    # def greetings(firstname, lastname):
    #     print("Hi {} {}! How are you?".format(firstname, lastname))
    # greetings('Ada', 'Lovelace')
    # greetings('Alan', 'Turing')
    # greetings(lastname='Lovelace', firstname='Ada')
    # greetings(firstname='Alan', lastname='Turing')

    # Return value
    # def greetings(name):
    #     print("Hi {}! How are you?".format(name))
    #     return len(name) >= 3
    # result = greetings('Ada')
    # print(result)

    # def greetings(name):
    #     print("Hi {}! How are you?".format(name))
    # greetings('Ada')
    # greetings('Michael')

    # def greetings():
    #     print("Hey! How are you?")
    # greetings()
    # greetings()