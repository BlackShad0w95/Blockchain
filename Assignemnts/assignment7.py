# 1) Create a Food class with a “name” and a “kind” attribute as well as a “describe() ” method (which prints “name” and “kind” in a sentence).
#

"""Class method"""
# class Food:
#     def __init__(self, name, kind):
#         self.name = name
#         self.kind = kind
#
#     def describe(self):
#         print("Name of the food is:{} and its kind:{}".format(self.name, self.kind))

#
# food = Food("Kiełbasa", "obiadowe")
# food.describe()
"""Init method"""
# class Food:
#     def __init__(self, name, kind):
#         self.name = name
#         self.kind = kind
#         self.describe()
#
#     def describe(self):
#         print("Name of the food is:{} and its kind:{}".format(self.name, self.kind))
#
#
# food = Food("Kiełbasa", "obiadowe")

# 2) Try turning describe()  from an instance method into a class and a static method. Change it back to an instance method thereafter.
#
"""Static method"""
#
#
# class Food:
#     def __init__(self, name, kind):
#         self.name = name
#         self.kind = kind
#
#     @staticmethod
#     def describe(name, kind):
#         print("Name of the food is:{} and its kind:{}".format(name, kind))
#
#
# food = Food("Kiełbasa", "obiadowe")
# Food.describe("Kaktusowy", "Sok")

"""Class method"""


# class Food:
#
#     # name = 'X'
#     # kind = 'Y'
#     def __init__(self, name, kind):
#         self.name = name
#         self.kind = kind
#
#     @classmethod
#     def describe(cls, name, kind):
#         print("Name of the food is:{} and its kind:{}".format(name, kind))
#
#
# # Food.name = "Banana"
# # Food.kind = "Fruit"
# # Food.describe()
# Food.describe('Banana', "fruit")

# 3) Create a  “Meat” and a “Fruit” class – both should inherit from “Food”. Add a “cook() ” method to “Meat” and “clean() ” to “Fruit”.
#
"""Init method"""


# class Food:
#     def __init__(self, name, kind):
#         self.name = name
#         self.kind = kind
#         self.describe()
#
#     def describe(self):
#         print("Name of the food is:{} and its kind:{}".format(self.name, self.kind))
#
#     def __repr__(self):
#         return "Name is: {}, kind is: {}".format(self.name, self.kind)
#
#
# class Meat(Food):
#     def __init__(self):
#         self.cook()
#         super().__init__(self.name, self.kind)
#
#     def cook(self):
#         print("I am cooking meat")
#
#
# class Fruit(Food):
#     def __init__(self, name, kind):
#         self.clean()
#         super().__init__(name=name, kind=kind)
#
#     def clean (self):
#         print("I am cleaning fruit")
#
#
# food = Food("Kiełbasa", "obiadowe")
# apple = Fruit("japko", "owocowe")
# print(food)
# print(apple)

# 4) Overwrite a “dunder” method to be able to print your “Food” class.
