class Auto:
    def __init__(self, merk, model):
        self.__merk = merk
        self.snelheid = 0
        self.model = model

    def versnellen(self, delta):
        self.snelheid += delta
        print(f" Dit is een { self.__merk, self.model } en hij rijd nu { self.snelheid } km/uur  " )

    def stoppen(self):
        self.snelheid = 0
        print(self.__merk, self.model, " is gestopt", "de snelheid is nu ", self.snelheid )

auto1 = Auto("BMW", 'X5')
auto2 = Auto("VW",'golf')

# print(auto1.snelheid)

auto1.versnellen(10)
auto2.versnellen(20)

# print(auto1.snelheid)

auto1.stoppen()

# print(auto1.snelheid)


auto1.versnellen(10)