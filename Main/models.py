from unicodedata import category
from django.db import models

# Create your models here.
class Producto(models.Model):
    titulo = models.CharField(max_length=40)
    categoria = models.CharField(max_length=30)
    precio = models.IntegerField()

class Usuario(models.Model):
    username = models.CharField(max_length=30)
    email = models.EmailField()

class Compras(models.Model):
    precio = models.IntegerField()
    titulo = models.CharField(max_length=40)
    fecha = models.DateField()
