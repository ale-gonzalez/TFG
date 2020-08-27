from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator


class Ciudad(models.Model):
    nombre = models.CharField(max_length=30)
    historia = models.CharField(max_length=500)
    localizacion = models.CharField(max_length=20)
    foto = models.FileField(null=True, upload_to="img/ciudad")
    visitantes = models.ManyToManyField(User, blank=True)

    def __str__(self):
        return self.nombre


class Monumento(models.Model):
    nombre = models.CharField(max_length=30)
    agno_inaguracion = models.CharField(max_length=9)
    historia = models.CharField(max_length=500)
    localizacion = models.CharField(max_length=20)
    precio_pers = models.PositiveIntegerField(default=0)
    precio_disc = models.PositiveIntegerField(default=0)
    foto = models.FileField(null=True, upload_to="img/monumento")

    def __str__(self):
        return self.nombre


class Valoracion(models.Model):
    calificacion = models.PositiveIntegerField(default=1, validators=[MaxValueValidator(100), MinValueValidator(1)])
    comentario = models.CharField(max_length=500)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    monumentos = models.ForeignKey(Monumento, on_delete=models.CASCADE)

    def __str__(self):
        return self.comentario


class Aparcamiento(models.Model):
    localizacion = models.CharField(max_length=20)

    def __str__(self):
        return self.localizacion


class Alojamiento(models.Model):
    nombre = models.CharField(max_length=30)
    calificacion = models.PositiveIntegerField(default=1, validators=[MaxValueValidator(100), MinValueValidator(1)])
    localizacion = models.CharField(max_length=20)
    foto = models.FileField(null=True, upload_to="img/alojamiento")

    def __str__(self):
        return self.nombre


class Linea(models.Model):
    origen = models.CharField(max_length=30)
    destino = models.CharField(max_length=30)

    def __str__(self):
        return self.origen + " - " + self.destino


class Barrio(models.Model):
    nombre = models.CharField(max_length=30)
    historia = models.CharField(max_length=500)
    localizacion = models.CharField(max_length=20)
    foto = models.FileField(null=True, upload_to="img/barrio")
    ciudad = models.ForeignKey(Ciudad, on_delete=models.CASCADE)
    aparcamientos = models.ForeignKey(Aparcamiento, on_delete=models.CASCADE)
    alojamientos = models.ForeignKey(Alojamiento, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre


class Parada(models.Model):
    nombre = models.CharField(max_length=30)
    localizacion = models.CharField(max_length=30)
    lineas = models.ManyToManyField(Linea)
    barrios = models.ForeignKey(Barrio, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre


class Transporte(models.Model):
    tipo = models.CharField(max_length=30)
    usuarios = models.ManyToManyField(User, blank=True)

    def __str__(self):
        return self.tipo
