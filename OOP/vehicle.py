
class Vehicle:

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