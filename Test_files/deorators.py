def make_pretty(func):
    def inner():
        print("I got decorated")
        func()
    return inner


@make_pretty
def ordinary():
    print("I am ordinary")


# pretty = make_pretty(ordinary)
# print(type(pretty))

# ordinary = make_pretty(ordinary)
ordinary()


# pretty()
# ordinary()


#
# pretty = make_pretty(ordinary())

# x = 5
# print(callable(x))
#
# def testFunction():
#   print("Test")
#
# y = testFunction
# print(callable(y))


def smart_divide(func):
    def inner(a, b):
        print("I am going to divide", a, "and", b)
        if b == 0:
            print("Whoops! cannot divide")
            return

        return func(a, b)
    return inner


@smart_divide
def divide(a, b):
    print(a/b)


divide(3, 0)