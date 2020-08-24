from django.contrib import admin
from .models import Usuario, Ciudad, Valoracion, Monumento, Barrio, Aparcamiento, Transporte, Lineas, Parada
# Register your models here.
admin.site.register(Usuario)
admin.site.register(Ciudad)
admin.site.register(Valoracion)
admin.site.register(Monumento)
admin.site.register(Barrio)
admin.site.register(Aparcamiento)
admin.site.register(Transporte)
admin.site.register(Lineas)
admin.site.register(Parada)