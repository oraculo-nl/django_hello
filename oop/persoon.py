# class Persoon:
#     def __init__(self, naam, leeftijd):
#         self.naam = naam
#         self.leeftijd = leeftijd
#
# class Docent(Persoon):
#     def __init__(self, naam, leeftijd, vak):
#         super().__init__(naam, leeftijd)
#         self.vak = vak
#
# docenten = [
#     Docent("Peter", 42, "Python"),
#     Docent("Bob", 50, "Wiskunde"),
# ]
#
# for docent in docenten:
#     print(f'Docent naam: {docent.naam}', f'Docent Leeftijd: {docent.leeftijd}', f'Vak: {docent.vak}')
#
class Persoon:
    def init(self, naam, leeftijd):
        self.naam = naam
        self.leeftijd = leeftijd
class Docent(Persoon):
    def init(self, naam, leeftijd, vak):
        super().__init__(naam, leeftijd)   # "Persoon, doe jij jouw deel"
        self.vak = vak                     # en ik doe mijn eigen deel
docenten = [Docent("Nick", 40, "Python"), Docent("Lisa", 35, "Django")]
for d in docenten:
    print(d.naam, d.vak)