my_name = input('Provide your name: ')
my_age = int(input('Provide your age: '))


def print_your_data():
    print('My name is {} and I am {} years old'.format(my_name, my_age))


def number_of_decades():
    decades = int(my_age / 10)
    return decades

print_your_data()
print(number_of_decades())
