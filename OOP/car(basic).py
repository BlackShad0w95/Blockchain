class SportCar:
    # top_speed = 100
    # warnings = []
    # duder method
    def __init__(self, starting_top_speed=100):
        self.top_speed = starting_top_speed
        self._warnings = []

    def __repr__(self):
        print("Printing..")
        return "Top speed:{}. Warnings:{}".format(self.top_speed, len(self._warnings))

    def __len__(self):
        return len(self._warnings)

    def drive(self):
        print("I am driving but certainly not faster than {}".format(self.top_speed))

    def add_warnings(self, warnings_text):
        if len(warnings_text) > 0:
            self._warnings.append(warnings_text)

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
