from django.contrib import admin
from .models import Ciudad, Valoracion, Monumento, Barrio, Aparcamiento, Transporte, Linea, Parada
# Register your models here
admin.site.register(Ciudad)
admin.site.register(Valoracion)
admin.site.register(Monumento)
admin.site.register(Barrio)
admin.site.register(Aparcamiento)
admin.site.register(Transporte)
admin.site.register(Linea)
admin.site.register(Parada)