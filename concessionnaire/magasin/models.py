from django.db import models
from django.shortcuts import reverse

#from magasin.views import Voiture, Facture


# Create your models here.

class Voiture(models.Model):
    no_serie = models.IntegerField(unique=True)
    marque = models.CharField(max_length=25)
    modele = models.CharField(max_length=25)
    COLOR_CHOICE = (
        ('Bl', 'Bleu'),
        ('Ro', 'Rouge'),
        ('Ja', 'Jaune'),
        ('No', 'Noir'),
        ('Blc', 'Blanc'),
        ('Gr', 'Gris'),
        ('Ve', 'Vert'),
    )
    couleur = models.CharField(max_length=4, choices=COLOR_CHOICE)
    annee = models.DateField()
    poids = models.IntegerField()
    prix = models.FloatField()

    def get_absolute_url(self):
        return reverse('magasin:voiture-detail', kwargs={'pk': self.pk})


class Facture(models.Model):
    voitureVendue = models.ForeignKey(
        'Voiture',
        on_delete=models.DO_NOTHING,
    )
    montant = models.FloatField()
    nom_acheteur = models.CharField(max_length=50)

    def get_absolute_url(self):
        return reverse('magasin:facture-detail', kwargs={'pk': self.pk})
