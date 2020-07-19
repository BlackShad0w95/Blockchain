class Celsius:
    def __init__(self, temperature = 0):
        self.temperature = temperature

    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32

    @temperature.getter
    def temperature(self):
        print("Getting value")
        return self._temperature

    @temperature.setter
    def temperature(self, value):
        if value < -273:
            raise ValueError("Temperature below -273 is not possible")
        print("Setting value")
        self._temperature = value

    # temperature = property(get_temperature, set_temperature)
    # # make empty property
    # temperature = property()
    # # assign fget
    # temperature = temperature.getter(get_temperature)
    # # assign fset
    # temperature = temperature.setter(set_temperature)

c=Celsius()