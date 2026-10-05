class Teller:
    __aantal = 0

    def __init__(self):
        Teller.__aantal += 1
        self.id = Teller.__aantal

    @property
    def aantal(self):
        return self.__aantal


print(Teller().aantal)
first = Teller()
print(Teller().aantal)
second = Teller()
print(Teller().aantal)

Teller().__aantal = 0

print(Teller().aantal)


transactie

bankrekening

tegenpartij


class Klas:
    def __init__(self):
        self.docenten = []
        self.kinderen = []

    def gymen(self):



