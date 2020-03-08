my_list = ['h', 'e', 'l', 'l', 'o']
my_text = 'hello'

for letter in my_text  :
    print(letter)
name = 'Domi'
age = 29
# One way
print("I am {1} I am balabaka {1}".format(name, age))
# Another way
print("I am {imie} I am balabaka {wiek}".format(imie=name, wiek=age))

# FORMAT

founds = 145.7878
print('Founds: {}'.format(founds))
print('Founds: {:f}'.format(founds))
print('Founds: {:.1f}'.format(founds))
print('Founds: {:10.1f}'.format(founds))
print('Founds: {:>10.1f}'.format(founds))
print('Founds: {:*^10.1f}'.format(founds))

#ESCAPE
print('I\'m a Domi')

# F methode
print(f'I\'m a {age:^10.2f} Domi')

#MAP
siple_list = [1, 2, 3, 4]


def multiply(el):
    return el * 2


print(list(map(multiply, siple_list)))

#LAMBDA

print(list(map(lambda el: el*2, siple_list)))


def myfunc(n):
  return lambda a : a * n


mydoubler = myfunc(2)
print(myfunc(2))
print(mydoubler(11))


# help(my_list)
# help(str)

# a = 10
#
#
# def changeit(b):
#     print('B value:{}'.format(b))
#     b = 100
#     print('B new value:{}'.format(b))
#
#
# changeit(a)
# print(a)