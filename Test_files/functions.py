def unlimited_arguments(args):
    for argument in args:
        print(argument)


my_list = [1, 2, 3, 4]
unlimited_arguments(my_list)


def unlimited_arguments2(*args):
    print(args)
    for argument in args:
        print(argument)


unlimited_arguments2(*[1, 2, 3, 4])


def unlimited_arguments3(**kwargs):
    print(kwargs)
    for key, value in kwargs.items():
        print(key, value)


unlimited_arguments3(name='Domi', age=24)

# named - dictionary
# unnamed - tuple