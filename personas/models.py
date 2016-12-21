from django.db import models
from django_countries.fields import CountryField

HOMBRE = "H"
MUJER = "M"

GENERO = (
    (HOMBRE, "Hombre"),
    (MUJER, "Mujer"),
)

SI = "S"
NO = "N"

PADRON = (
    (SI, 'Si'),
    (NO, 'No'),
)


class Persona(models.Model):

    dni = models.CharField(max_length=9, blank=False)  # DNI-NIE de la persona(obligatorio)
    nombre = models.CharField(max_length=100, blank=False)  # Nombre de la persona (obligatorio)
    primer_apellido = models.CharField(max_length=100, blank=False)  # Primer apellido de la persona (obligatorio)
    segundo_apellido = models.CharField(max_length=100)  # Segundo apellido de la persona
    sexo = models.CharField(max_length=1, choices=GENERO, default=HOMBRE)  # Sexo de la persona
    fecha_nacimiento = models.DateField()  # Fecha de nacimiento de la persona
    pais = CountryField()
    direccion = models.CharField(max_length=100)  # Dirección de la persona
    telefono = models.CharField(max_length=9)  # Teléfono de la persona
    empadronamiento = models.CharField(max_length=1, choices=PADRON, default=NO)
    fecha_alta = models.DateTimeField(auto_now_add=True)  # Guarda la fecha de alta de la persona (automática)
    fecha_modificacion = models.DateTimeField(auto_now=True)  # Guarda la fecha de la última modificación de la ficha

    def __str__(self):
        return self.nombre
