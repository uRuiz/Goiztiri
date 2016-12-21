from django.db import models


class Municipio(models.Model):

    codigo_postal = models.CharField(max_length=5)
    nombre = models.CharField(max_length=30)

    def __str__(self):
        return self.nombre

