from django.contrib import admin
from .models import Ciudad, Valoracion, Monumento, Barrio, Aparcamiento, Transporte, Linea, Parada
from easy_maps.widgets import AddressWithMapWidget
from .forms import ModelForm
# Register your models here


class CiudadAdmin(admin.ModelAdmin):
    class form(ModelForm):
        class Meta:
            widgets = {
                'localizacion': AddressWithMapWidget({'class': 'vTextField'})
            }

class MunmemntoAdmin(admin.ModelAdmin):
    class form(ModelForm):
        class Meta:
            widgets = {
                'localizacion': AddressWithMapWidget({'class': 'vTextField'})
            }



admin.site.register(Ciudad,  CiudadAdmin)
admin.site.register(Valoracion)
admin.site.register(Monumento, MunmemntoAdmin)
admin.site.register(Barrio)
admin.site.register(Aparcamiento)
admin.site.register(Transporte)
admin.site.register(Linea)
admin.site.register(Parada)

