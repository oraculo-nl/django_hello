# members/models.py
from django.db import models
class Member(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=30)
    joined_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.first_name} {self.last_name}"


# budget/models.py
from django.db import models
class Transactie(models.Model):
    rekeningnummer = models.CharField(max_length=20)
    transactiedatum = models.DateField()
    bedrag = models.DecimalField(max_digits=10, decimal_places=2)
    omschrijving = models.TextField()
    categorie = models.CharField(max_length=50, default='Overig')
def __str__(self):
    return f"{self.transactiedatum} | {self.bedrag} | {self.omschrijving[:40]}"