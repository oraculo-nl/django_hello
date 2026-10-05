class Auto:
    def __init__(self, merk): # constructor
        self.merk = merk
    def versnellen(self, snelheid):
        print(f"Ik ben een {self.merk} en versnel met {snelheid} km per uur")
    def __str__(self):
        return f"Ik ben een {self.merk}"

auto1 = Auto("BMW")  # instantie van 1 auto maken
#
# auto.versnellen(100)

class Vrachtwagen(Auto):
    def __init__(self, merk, snelheid):
        super().__init__(merk)
        self.snelheid = snelheid


auto2 = Auto("VW")

showroom = [auto1,auto2]

print(showroom)
for auto in showroom:
    print(auto)

print(showroom[1].merk)

