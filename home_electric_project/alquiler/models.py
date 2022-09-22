from django.db import models
from django.contrib.auth.models import User

# Create your models heree
class Herramienta(models.Model):
    nombre = models.CharField(max_length=50)
    disponibilidad = models.BooleanField()
    
    def __str__(self) -> str:
        return self.nombre

class Alquiler(models.Model):
    inicio = models.DateField(default='2022-01-01')
    fin = models.DateField(default='2022-01-01')
    usuario= models.ForeignKey(User, on_delete=models.CASCADE)
    herramienta= models.ForeignKey(Herramienta, on_delete=models.CASCADE)

