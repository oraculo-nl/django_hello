class Bankrekening:
    def __init__(self, naam):
        self.__naam = naam
        self.__saldo = 0

    def stort(self, bedrag, silent = False):
        self.__saldo += bedrag
        if not silent:
            print(f"> { bedrag } gestort op rekening { self.__naam } ")

    def opname(self, bedrag, silent = False):
        if bedrag <= self.__saldo:
            self.__saldo -= bedrag
            if not silent:
                print(f"> {bedrag} opgenomen van rekening {self.__naam} ")
        else:
            print("> Saldo is te laag voor zo een grote opname !!")

    def toon_saldo(self):
        print(f"> Het huidige saldo van de rekening met de naam {  self.__naam } is : { self.__saldo } ")
print("")
print("> ")
rekening = Bankrekening("'Geheime'")

rekening.toon_saldo()
rekening.stort(100, True)
rekening.opname(150, True)
rekening.stort(100, True)
rekening.opname(150, True)

rekening.toon_saldo()
print("> ")

rekening2 = Bankrekening("'Dagelijkse'")
rekening2.toon_saldo()
rekening2.stort(100)
rekening2.opname(150)
rekening2.stort(100)
rekening2.opname(150)

rekening.toon_saldo()
print("> ")