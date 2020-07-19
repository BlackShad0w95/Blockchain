# class A(object):
#     def foo(self, x):
#         print("executing foo(%s, %s)" % (self, x))
#
#     @classmethod
#     def class_foo(cls, x):
#         print("executing class_foo(%s, %s)" % (cls, x))
#
#     @staticmethod
#     def static_foo(x):
#         print("executing static_foo(%s)" % x)
#
# a = A()
# a.foo(1)
# a.class_foo(1)
# A.class_foo(1)

class Owoc:

    def __init__(self, nazwa, kolor, twardosc, obieraczka):
        self.nazwa = nazwa
        self.kolor = kolor
        self.twardosc = twardosc
        self.obieraczka = obieraczka

    @classmethod
    def obieranie(cls, nazwa, kolor):
        print("Obieram {} {}.".format(nazwa, kolor))

banan = Owoc('banan', 'zółty', 'twardy', True)

Owoc.obieranie('banan', 'zolty')
