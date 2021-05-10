from django.contrib import admin
from django.urls import include, path
from . import views

app_name = 'handitour'

urlpatterns = [
    path('', views.ciudades, name="raiz"),
    path('inicio/', views.ciudades, name="inicio"),
    path('autenticacion/', views.login_usuario, name="login"),
    path('logout/', views.logout_usuario, name="logout"),
    path('ciudad/<id>/', views.ciudad_monumento, name="ciudad_monumento"),
    path('monumento/<id>/', views.detalle_monumento, name="monumento_detalle"),
    path('alojamientos/<id>/', views.ciudad_alojamiento, name="ciudad_alojamiento"),
    path('alojamiento/<id>/', views.detalle_alojamiento, name="alojamiento_detalle"),
    path('aparcamientos/<id>/', views.ciudad_aparcamiento, name="ciudad_aparcamiento"),
]
