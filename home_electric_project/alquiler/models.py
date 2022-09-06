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
        return self.primer_nombre, self.primer_apellido, self.direccion, self.email, self.tlfno, self.cedula
    
class Alquiler(models.Model):
    inicio = models.DateField()
    fin = models.DateField()
    usuario= models.ForeignKey(Usuario, on_delete=models.CASCADE)
    herramienta= models.ForeignKey(Herramienta, on_delete=models.CASCADE)
    
    #def __str__(self):
    #    return f'{self.inicio}'
