from django.contrib import admin
from django.urls import include, path
from . import views
urlpatterns = [
    path('inicio/', views.ciudades, name="inicio"),
    path('login/', views.login_usuario, name="login"),
    path('logout/', views.logout_usuario, name="logout"),
    path('registro/', views.alta_usuario, name="registro"),
]
