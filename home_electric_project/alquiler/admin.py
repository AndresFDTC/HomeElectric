from django.contrib import admin
from alquiler.models import Herramienta, Alquiler
# Register your models here.

class Herramienta_admin(admin.ModelAdmin):
    list_display=('nombre', 'disponibilidad')
    
class Alquiler_admin(admin.ModelAdmin):
    list_display=('inicio', 'fin', 'usuario', 'herramienta') 
    
admin.site.register(Herramienta, Herramienta_admin)
admin.site.register(Alquiler, Alquiler_admin)
