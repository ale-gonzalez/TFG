from django.shortcuts import render
from .models import Ciudad
# Create your views here.

def ciudades (request):
    ciudades = Ciudad.objects.all()
    return render(request, "index.html", {"ciudades":ciudades})
