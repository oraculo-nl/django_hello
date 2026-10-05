class Bankrekening:
    def __init__(self):
        self.__saldo = 0.00
    def stort(self, bedrag=0.00):
        if bedrag > 0.00:
            self.__saldo += bedrag
        return self.__saldo
    def opname(self, bedrag=0.00):
        if self.__saldo - bedrag >= 0.00:
            self.__saldo -= bedrag
            return self.__saldo
        else:
            return "Onvoldoende saldo"
    def saldo(self):
        return self.__saldo
rekening = Bankrekening()
print(rekening.stort(5.00))
print(rekening.opname(3.50))
print(rekening.saldo())
print(rekening.stort())
print(rekening.opname(10))