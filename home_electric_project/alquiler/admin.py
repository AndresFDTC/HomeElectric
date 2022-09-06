from django.contrib import admin
from alquiler.models import Herramienta, Usuario, Alquiler
# Register your models here.

class Herramienta_admin(admin.ModelAdmin):
    list_display=('nombre', 'disponibilidad')
     
class Usuario_admin(admin.ModelAdmin):
    list_display=('primer_nombre', 'primer_apellido', 'email', 'tlfno', 'direccion', 'cedula')
    
class Alquiler_admin(admin.ModelAdmin):
    list_display=('inicio', 'fin', 'usuario', 'herramienta') 
    
admin.site.register(Herramienta, Herramienta_admin)
admin.site.register(Usuario, Usuario_admin)
admin.site.register(Alquiler, Alquiler_admin)
