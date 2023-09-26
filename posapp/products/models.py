from django.db import models

class Nevado(models.Model):
    nombre = models.CharField(max_length=255)
    tipo = models.CharField(max_length=255)
    vaso = models.PositiveIntegerField(default=1)
    pitillo = models.PositiveBigIntegerField(default=1)
    precio = models.DecimalField(max_digits=10, decimal_places=0)

class Taco(models.Model):
    nombre = models.CharField(max_length=255)
    carne = models.CharField(max_length=255)
    pesocarne = models.DecimalField(max_digits=5, decimal_places=0)
    precio = models.DecimalField(max_digits=10, decimal_places=0)
# Create your models here.
