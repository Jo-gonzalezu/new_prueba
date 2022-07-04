from django.db import models

# Create your models here.
class Productos(models.Model):
    codigo = models.IntegerField()
    nombre = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=30)
    disponible = models.BooleanField()
    fechaIncorporacion = models.DateField()
    correoProveedor = models.EmailField()
    imagen = models.CharField(max_length=254)
    precio = models.IntegerField()

class cliente(models.Model):
    rut = models.IntegerField()
    nombre = models.CharField(max_length=30)
    apellidoPa = models.CharField(max_length=30)
    apellidoMa = models.CharField(max_length=30)
    nacimiento = models.DateField()
    correo = models.EmailField()
    

class boleta(models.Model):
    nroBoleta = models.IntegerField()
    cantidadProductos = models.IntegerField()
    total = models.FloatField()
    fecha = models.DateField()
    
class usuario(models.Model):
    correo = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    
