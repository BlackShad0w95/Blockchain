def increment(a):
    a += 1
    print(id(a))


num = 1
increment(num)
print(num)
print(id(num))


def add_more (l):
    l.append(5)
    print(l)
    print('ID of l')
    print(id(l))


my_list = [1, 2, 3, 4]
add_more(my_list)
print(my_list)
print("ID of my list after add more")
print(id(my_list))