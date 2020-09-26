from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.urls import reverse


class Ciudad(models.Model):
    nombre = models.CharField(max_length=30)
    historia = models.TextField(max_length=500)
    localizacion = models.CharField(max_length=100)
    visitantes = models.ManyToManyField(User, blank=True)
    foto = models.FileField(null=True, upload_to="img/ciudad")

    def get_absolute_url(self):
        return reverse("ciudad_monumento", args=[self.id])

    def __str__(self):
        return self.nombre



class Valoracion(models.Model):
    calificacion = models.PositiveIntegerField(default=1, validators=[MaxValueValidator(100), MinValueValidator(1)])
    comentario = models.CharField(max_length=500)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    monumentos = models.ForeignKey("Monumento", on_delete=models.CASCADE)

    def __str__(self):
        return self.comentario


class Aparcamiento(models.Model):
    localizacion = models.CharField(max_length=100)
    barrio = models.ForeignKey("Barrio", null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.localizacion


class Alojamiento(models.Model):
    nombre = models.CharField(max_length=30)
    calificacion = models.PositiveIntegerField(default=1, validators=[MaxValueValidator(100), MinValueValidator(1)])
    localizacion = models.CharField(max_length=100)
    foto = models.FileField(null=True, upload_to="img/alojamiento")
    barrio = models.ForeignKey("Barrio", null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre


class Linea(models.Model):
    numero_nombre = models.CharField(max_length=30)
    origen = models.CharField(max_length=30)
    destino = models.CharField(max_length=30)
    transporte = models.ForeignKey("Transporte", null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.numero_nombre + ":" + self.origen + " - " + self.destino


class Barrio(models.Model):
    nombre = models.CharField(max_length=30)
    historia = models.TextField(max_length=500)
    localizacion = models.CharField(max_length=100)
    foto = models.FileField(null=True, upload_to="img/barrio")
    ciudad = models.ForeignKey("Ciudad", on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre


class Monumento(models.Model):
    nombre = models.CharField(max_length=30)
    agno_inaguracion = models.CharField(max_length=9)
    historia = models.TextField(max_length=500)
    localizacion = models.CharField(max_length=100)
    precio_pers = models.DecimalField(default=0, max_digits=4, decimal_places=2)
    precio_disc = models.DecimalField(default=0, max_digits=4, decimal_places=2)
    barrio = models.ForeignKey("Barrio", null = True, on_delete=models.CASCADE)
    foto = models.FileField(null=True, upload_to="img/monumento")

    def __str__(self):
        return self.nombre


class Parada(models.Model):
    nombre = models.CharField(max_length=30)
    localizacion = models.CharField(max_length=100)
    lineas = models.ManyToManyField("Linea")
    barrio = models.ForeignKey("Barrio", on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre


class Transporte(models.Model):
    tipo = models.CharField(max_length=30)
    usuarios = models.ManyToManyField(User, blank=True)

    def __str__(self):
        return self.tipo
