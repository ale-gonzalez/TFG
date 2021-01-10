from django.shortcuts import render, redirect, get_object_or_404, reverse
from .models import Ciudad, Monumento
from .forms import LoginForm, AltaForm, ValoracionForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.


def ciudades (request):
    ciudades = Ciudad.objects.all()
    return render(request, "index.html", {"ciudades": ciudades, "encabezado": "HANDITOUR"})


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
    return redirect('/inicio')


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


def ciudad_monumento(request, id):
    ciudad = get_object_or_404(Ciudad, id=id)
    monumentos = Monumento.objects.filter(barrio__ciudad=ciudad)
    return render(request, "ciudad.html", {"monumentos": monumentos, "encabezado": ciudad.nombre.upper(), "ciudad":  ciudad})


def detalle_monumento(request, id):
    monumento = get_object_or_404(Monumento, id=id)
    if request.POST:
        form = ValoracionForm(request.POST)
        if form.is_valid():
            form.save()
            return reverse("handitour:monumento_detalle", args=[id])
            #return redirect("/monumento/"+id+"/")
        else:
            return render(request, "monumento.html", {"monumento": monumento, "encabezado": monumento.nombre.upper(), "form": form})
    else:
        form = ValoracionForm()
        return render(request, "monumento.html", {"monumento": monumento, "encabezado": monumento.nombre.upper(), "form": form} )


@login_required()
def comentario(request):
    if request.POST:
        form = ValoracionForm(request.POST)
        if form.is_valid():
            comentario = form.save()
            return redirect('/inicio')
        else:
            return render(request, "monumento.html", {'form': form})
    else:
        form = ValoracionForm()
        return render(request, "monumento.html", {'form': form})
