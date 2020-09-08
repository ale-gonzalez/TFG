from django.shortcuts import render, redirect
from .models import Ciudad
from .forms import LoginForm, AltaForm
from django.contrib.auth import authenticate, login, logout, get_user
from django.contrib.auth.decorators import login_required

# Create your views here.

def ciudades (request):
    ciudades = Ciudad.objects.all()
    return render(request, "index.html", {"ciudades":ciudades})


def login_usuario(request):
    if request.POST:
        form = LoginForm(request.POST)
        username = request.POST['usuario']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/inicio/')
        else:
            form = LoginForm()
            return render(request, "login_form.html", {'form': form})
    else:
        form = LoginForm()
        return render(request, "login_form.html", {'form': form})

@login_required
def logout_usuario(request):
    logout(request)
    return redirect('/login/')

def alta_usuario(request):
    if request.POST:
        form = AltaForm(request.POST)
        if form.is_valid():
            alta = form.save()
            return redirect('/login')
        else:
            return render(request, "altausuario_form.html", {'form': form})
    else:
        form = AltaForm()
        return render(request, "altausuario_form.html", {'form': form})
