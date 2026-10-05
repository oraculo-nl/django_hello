class Teller:
    aantal = 0
    def __init__(self):
        Teller.aantal += 1
        self.id = Teller.aantal

a = Teller() # wordt __init__ aangeroepen
b = Teller() # wordt __init__ aangeroepen
print(Teller.aantal)
print(a.id, b.id)