from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Usuario (models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=30)
    email = models.CharField(max_length=100)
    edad = models.IntegerField(max_length=2)
    password = models.CharField(max_length=30)
    foto = models.FileField(null=True, upload_to="img/usuario")

    def __str__(self):
        return self.nombre

class Ciudad (models.Model):
    nombre = models.CharField(max_length=30)
    historia = models.CharField(max_length=500)
    localizacion = models.CharField(max_length=20)
    foto = models.FileField(null=True, upload_to="img/ciudad")
    usuarios = models.ManyToManyField(Usuario, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

class Monumento (models.Model):
    nombre = models.CharField(max_length=30)
    agno_inniaguracion = models.IntegerField (default=1, MaxValue=2020, MinValue=-10000)
    historia = models.CharField(max_length=500)
    localizacion = models.CharField(max_length=20)
    precio_pers = models.PositiveIntegerField(default=0, max_length=2)
    precio_disc = models.PositiveIntegerField(default=0, max_length=2)
    foto = models.FileField(null=True, upload_to="img/ciudad")

    def __str__(self):
        return self.nombre

class Valoracion (models.Model):
    calificacion = models.PositiveIntegerField(default=1, MaxValue=100, MinValue=1)
    comentario = models.CharField(max_length=500)
    usuarios = models.ManyToManyField(Usuario, on_delete=models.CASCADE)
    monumento = models.ForeignKey(Monumento, on_delete=models.CASCADE())

    def __str__(self):
        return self.comentario


class Aparcamiento(models.Model):
    localizacion = models.CharField(max_length=20)

    def __str__(self):
        return self.localizacion

class Alojamiento (models.Model):
    nombre = models.CharField(max_length=30)
    calificacion = models.PositiveIntegerField(default=1, MaxValue=100, MinValue=1)
    localizacion = models.CharField(max_length=20)
    foto = models.FileField(null=True, upload_to="img/alojamiento")

    def __str__(self):
        return self.nombre

class Lineas (models.Model):
    origen = models.CharField(max_length=30)
    destino = models.CharField(max_length=30)

    def __str__(self):
        return self.origen + " " + self.destino


class Parada (models.Model):
    nombre = models.CharField(max_length=30)
    localizacion = models.CharField(max_length=30)
    lineas = models.ManyToManyField(Lineas, on_delete=models.Model)

    def __str__(self):
        return self.nombre

class Barrio (models.Model):
    nombre = models.CharField(max_length=30)
    historia = models.CharField(max_length=500)
    localizacion = models.CharField(max_length=20)
    foto = models.FileField(null=True, upload_to="img/barrio")
    ciudad = models.ForeignKey(Ciudad, on_delete=models.CASCADE)
    aparcamientos = models.ForeignKey(Aparcamiento, on_delete=models.CASCADE)
    alojamientos = models.ForeignKey(Alojamiento, on_delete=models.CASCADE)
    paradas = models.ForeignKey(Parada, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

class Transporte (models.Model):
    tipo = models.CharField(max_length=30)
    usuarios = models.ManyToManyField(Usuario, on_delete=models.CASCADE)

    def __str__(self):
        return self.tipo

