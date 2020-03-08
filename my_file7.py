def reassign (list):
    list = [0,1]
    print("List id")
    print(id(list))


def multiply(el):
    return el*2


lista = [2, 3]
print(lista)
reassign(lista)
print(lista)
print("New id")
print(id(lista))
multiply(lista)
print(lista)

for e in lista:
    e = multiply(e)
    print(e)
    print(lista)

