from django.db import models

# Create your models here.

class Transactie(models.Model):
    rekeningnummer = models.CharField(max_length=20)
    transactiedatum = models.DateField()
    bedrag = models.DecimalField(max_digits=10, decimal_places=2)
    omschrijving = models.TextField()
    categorie= models.CharField(max_length=50, default='Overig')

    def __str__(self):
        return f"{self.transactiedatum} | {self.bedrag} | {self.omschrijving[:40]}"