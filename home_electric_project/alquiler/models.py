from django.db import models

# Create your models heree
class Herramienta(models.Model):
    nombre = models.CharField(max_length=50)
    disponibilidad = models.BooleanField()
    
    def __str__(self) -> str:
        return self.nombre

class Usuario(models.Model):
    primer_nombre = models.CharField(max_length=30)
    segundo_nombre = models.CharField(max_length=30)
    primer_apellido = models.CharField(max_length=30)
    segundo_apellido = models.CharField(max_length=30)
    direccion = models.CharField(max_length=50)
    email = models.EmailField()
    tlfno = models.CharField(max_length=10)
    cedula = models.IntegerField()
    
    def __str__(self) -> str:
        return self.primer_nombre
    
class Alquiler(models.Model):
    inicio = models.DateField(default='2022-01-01')
    fin = models.DateField(default='2022-01-01')
    usuario= models.ForeignKey(Usuario, on_delete=models.CASCADE)
    herramienta= models.ForeignKey(Herramienta, on_delete=models.CASCADE)

