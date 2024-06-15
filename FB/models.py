from django.db import models

# Create your models here.


class Muntu(models.Model):
    nom = models.CharField(max_length=255)
    mot_de_passe = models.CharField(max_length=255)
    class Meta:
        verbose_name = ("Muntu")
        verbose_name_plural = ("Personnes")

    def __str__(self):
        return self.nom