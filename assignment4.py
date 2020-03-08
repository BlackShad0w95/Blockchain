# 1) Write a normal function that accepts another function as an argument. Output the result of that other function in your “normal” function.


def normal_function(dodane_wartosci):
    print(dodane_wartosci(10))


# 2) Call your “normal” function by passing a lambda function – which performs any operation of your choice – as an argument.


normal_function(lambda a: a*3)


# 3) Tweak your normal function by allowing an infinite amount of arguments on which your lambda function will be executed.


def normal_function2(dodane_wartosci, *args):
    for arg in args:
        print(dodane_wartosci(arg))


normal_function2(lambda a: a*3, 20, 3, 3, 3)

# 4) Format the output of your “normal” function such that numbers look nice and are centered in a 20 character column.


def normal_function3(dodane_wartosci, *args):
    for arg in args:
        print('Result: {:^20}'.format(dodane_wartosci(arg)))


normal_function3(lambda a: a*3, 20, 3, 3, 3)