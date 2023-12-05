from django.db import models

class Livre(models.Model):
    nom = models.CharField(max_length=255)
    auteur = models.CharField(max_length=255)
    date_publication = models.DateField()
    note = models.DecimalField(max_digits=3, decimal_places=2)

    def __str__(self):
        return self.nom
