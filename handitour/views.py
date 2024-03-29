from django.shortcuts import render, redirect, get_object_or_404, reverse
from .models import Ciudad, Monumento, Valoracion, Alojamiento, Barrio, Aparcamiento, Parada, Linea
from .forms import LoginForm, AltaForm, ValoracionForm, FiltroForm
from django.contrib.auth import authenticate, login, logout, get_user
from django.contrib.auth.decorators import login_required

# Create your views here.


def ciudades (request):
    ciudades = Ciudad.objects.all()
    return render(request, "index.html", {"ciudades": ciudades, "encabezado": "HANDITOUR"})


def login_usuario(request):
    if request.POST:
        formLogin = LoginForm(request.POST)
        formAlta = AltaForm(request.POST)
        if formLogin.is_valid():
            username = request.POST['usuario']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/inicio/')
            else:
                formLogin = LoginForm()
                return render(request, "autenticion_forms.html", {'formLogin': formLogin, 'formAlta': formAlta, "encabezado": "HANDITOUR"})
        if formAlta.is_valid():
            formAlta = formAlta.save()
            return redirect('/autenticacion')
            return render(request, "autenticion_forms.html", {'formLogin': formLogin, 'formAlta': formAlta, "encabezado": "HANDITOUR"})

    formLogin = LoginForm(request.POST)
    formAlta = AltaForm(request.POST)
    return render(request, "autenticion_forms.html", {'formLogin': formLogin, 'formAlta': formAlta, "encabezado": "HANDITOUR"})



@login_required
def logout_usuario(request):
    logout(request)
    return redirect('/inicio')


def ciudad_monumento(request, id):
    ciudad = get_object_or_404(Ciudad, id=id)
    monumentos = Monumento.objects.filter(barrio__ciudad=ciudad)
    return render(request, "ciudad.html", {"monumentos": monumentos, "encabezado": "HANDITOUR", "ciudad":  ciudad})


def detalle_monumento(request, id):
    monumento = get_object_or_404(Monumento, id=id)
    comentarios = Valoracion.objects.all().filter(monumento_id=id)
    ciudad = monumento.barrio.ciudad
    if request.POST:
        form = ValoracionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse("handitour:monumento_detalle", args=[id]))
        else:
            return render(request, "monumento.html", {"monumento": monumento, "encabezado": "HANDITOUR", "form": form, "comentarios": comentarios, "ciudad": ciudad})
    else:
        form = ValoracionForm(initial={'usuario':get_user(request),'monumento':monumento})
        return render(request, "monumento.html", {"monumento": monumento, "encabezado": "HANDITOUR", "form": form, "comentarios": comentarios, "ciudad": ciudad})


def ciudad_alojamiento(request, id):
    ciudad = get_object_or_404(Ciudad, id=id)
    alojamientos = Alojamiento.objects.filter(barrio__ciudad=ciudad)
    form = FiltroForm(ciudad.id, request.POST)
    if request.POST:
        if form.is_valid():
            seleccionado = form.cleaned_data.get('barrio')
            barrio = Barrio.objects.all().filter(nombre=seleccionado)[0]
            alojamientos = Alojamiento.objects.all().filter(barrio=barrio)
            return render(request, "alojamientos.html", {"alojamientos": alojamientos, "encabezado": "HANDITOUR", "ciudad": ciudad, "form": form, "barrio": barrio})
    else:
        form = FiltroForm(ciudad.id, request.POST)
        return render(request, "alojamientos.html", {"alojamientos": alojamientos, "encabezado": "HANDITOUR", "ciudad": ciudad, "form": form})


def detalle_alojamiento(request, id):
    alojamiento = get_object_or_404(Alojamiento, id=id)
    ciudad = alojamiento.barrio.ciudad
    return render(request, "alojamiento.html", {"alojamiento": alojamiento, "encabezado": "HANDITOUR", "ciudad": ciudad})

def ciudad_aparcamiento(request, id):
    ciudad = get_object_or_404(Ciudad, id=id)
    aparcamientos = Aparcamiento.objects.filter(barrio__ciudad=ciudad)
    form = FiltroForm(ciudad.id, request.POST)
    if request.POST:
        if form.is_valid():
            seleccionado = form.cleaned_data.get('barrio')
            barrio = Barrio.objects.all().filter(nombre=seleccionado)[0]
            aparcamientos = Aparcamiento.objects.all().filter(barrio=barrio)
            return render(request, "aparcamientos.html", {"aparcamientos": aparcamientos, "encabezado": "HANDITOUR", "ciudad": ciudad, "form": form, "barrio": barrio})
    else:
        form = FiltroForm(ciudad.id, request.POST)
        return render(request, "aparcamientos.html",  {"aparcamientos": aparcamientos, "encabezado": "HANDITOUR", "ciudad": ciudad, "form": form})


def transportes(request, id):
    ciudad = get_object_or_404(Ciudad, id=id)
    form = FiltroForm(ciudad.id, request.POST)
    paradas = Parada.objects.all().filter(barrio__ciudad=ciudad)
    if request.POST:
        if form.is_valid():
            seleccionado = form.cleaned_data.get('barrio')
            barrio = Barrio.objects.all().filter(nombre=seleccionado)[0]
            paradas = Parada.objects.all().filter(barrio=barrio)
            return render(request, "transportes.html", {"encabezado": "HANDITOUR", "ciudad": ciudad, "form": form, "barrio": barrio, "paradas": paradas})
    else:
        form = FiltroForm(ciudad.id, request.POST)
        return render(request, "transportes.html", {"encabezado": "HANDITOUR", "ciudad": ciudad, "form": form, "paradas": paradas})
