from django.db import models

# Create your models heree
class Herramienta(models.Model):
    nombre = models.CharField(max_length=50)
    disponibilidad = models.BooleanField()
    
class Alquiler(models.Model):
    inicio = models.DateField()
    fin = models.DateField()
    
class Usuario(models.Model):
    primer_nombre = models.CharField(max_length=30)
    segundo_nombre = models.CharField(max_length=30)
    primer_apellido = models.CharField(max_length=30)
    segundo_apellido = models.CharField(max_length=30)
    direccion = models.CharField(max_length=50)
    email = models.EmailField()
    tlfno = models.CharField(max_length=10)
    cedula = models.IntegerField(max_length=10)
    
    
