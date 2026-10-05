class Bankrekening:
    def __init__(self, rekeningnummer, saldo=0):
        self.rekeningnummer = rekeningnummer
        self.__saldo = saldo  # Private attribuut (met dubbele underscore)

    # Property voor alleen-lezen (Read-only property)
    @property
    def saldo(self):
        """Geeft het huidige saldo terug (alleen-lezen)."""
        return self.__saldo

    # Methode om geld zuiver op te storten
    def stort(self, bedrag):
        if bedrag > 0:
            self.__saldo += bedrag
            print(f"Er is €{bedrag} gestort. Nieuw saldo: €{self.__saldo}")
        else:
            print("Fout: Het stortingsbedrag moet groter zijn dan 0!")

    # Methode om geld op te nemen met controle op het saldo
    def opname(self, bedrag):
        if bedrag <= 0:
            print("Fout: Het opnamebedrag moet groter zijn dan 0!")
        elif bedrag > self.__saldo:
            print(f"Fout: Onvoldoende saldo! Huidig saldo is: €{self.__saldo}")
        else:
            self.__saldo -= bedrag
            print(f"Er is €{bedrag} opgenomen. Nieuw saldo: €{self.__saldo}")


# ==========================================
# Testen van de klasse (Gebruik van het object)
# ==========================================

# 1. Een nieuwe bankrekening aanmaken met €50 beginsaldo
rekening1 = Bankrekening("NL91ABNA0123456789", 50)

# 2. Het saldo uitlezen via de property (alleen-lezen)
print(f"Beginsaldo: €{rekening1.saldo}")

# Direct het saldo aanpassen werkt niet vanwege encapsulation:
# rekening1.saldo = 1000  --> Geef een AttributeError!

# 3. Geld storten
rekening1.stort(30)   # Saldo wordt €80

# 4. Geld opnemen met controles
rekening1.opname(40)  # Succesvol (Saldo wordt €40)
rekening1.opname(100) # Foutmelding: Onvoldoende saldo!
rekening1.stort(-10)  # Foutmelding: Ongeldig bedrag!