class SportCar:
    # top_speed = 100
    # warnings = []
    # duder method
    def __init__(self, starting_top_speed=100):
        self.top_speed = starting_top_speed
        self.warnings = []

    def __repr__(self):
        print("Printing..")
        return "Top speed:{}. Warnings:{}".format(self.top_speed, len(self.warnings))

    def drive(self):
        print("I am driving but certainly not faster than {}".format(self.top_speed))


car1 = SportCar()
car1.drive()
car1.warnings.append("New worning")


SportCar.top_speed = 200

car2 = SportCar(250)
car2.drive()
print(car2.warnings)

print(id(car1))
print(id(car2))
# warning - reference type - every instance of the class point for the same place in memory
print(id(car1.warnings))
print(id(car2.warnings))
print(car1.__dict__)
print(car1)

# L=[]
# print(dir(L))
# help(L)
