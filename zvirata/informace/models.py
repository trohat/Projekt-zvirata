from django.db import models

# Create your models here.

class Zvire(models.Model):
    druh = models.CharField(max_length=100)
    jmeno = models.CharField(max_length=200)
    popis = models.CharField(max_length=500)
    vek = models.IntegerField()

    def __str__(self):
        return f"{self.druh} {self.jmeno} ({self.vek})"

