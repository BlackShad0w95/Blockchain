from vehicle import Vehicle


class SportCar (Vehicle):

    def brag(self):
        print("Look how cool my car is")


car1 = SportCar()
car1.drive()
car1.add_warnings("New worning")
car1._warnings.append("OK")

SportCar.top_speed = 200

car2 = SportCar(250)
car2.drive()


print(id(car1))
print(id(car2))
# warning - reference type - every instance of the class point for the same place in memory

print(car1.__dict__)
print(car1)
print(len(car1))
print(car1._warnings)

# L=[]
# print(dir(L))
# help(L)
