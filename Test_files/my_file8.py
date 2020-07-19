class Nwm:
    liczba_kotow = 88

    def __init__(self, liczba_kotow):
        self._liczba_kotow = liczba_kotow
        print("Ola ma kota{}".format(self.liczba_kotow))


nwm = Nwm(5)
print (nwm.__dict__)
