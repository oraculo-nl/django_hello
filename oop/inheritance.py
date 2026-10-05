class Dier:
    def __init__(self, naam):
        self.naam = naam
    def geluid(self):
        return "..."


class Hond(Dier):
    pass

class Kat(Dier):
    def geluid(self):
        return "Miauw!"


h = Hond("Fido")


k = Kat("Simba")


dieren = [h,k]


for dier in dieren:
    print(dier.geluid())

