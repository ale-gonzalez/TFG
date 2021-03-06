from django.forms import ModelForm, ModelChoiceField
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Valoracion, Ciudad, Barrio
from django.shortcuts import get_object_or_404

class LoginForm(forms.Form):
    usuario = forms.CharField(label='Usuario',
                              widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Usuario'}))
    password = forms.CharField(label='Contraseña',
                               widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Contraseña'}))


class AltaForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        labels = {'username': "Usuario", 'first_name': "Nombre", 'last_name': "Apellidos", 'email': "Correo"}

    def __init__(self, *args, **kwargs):
        super(AltaForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})


class ValoracionForm(ModelForm):
    class Meta:
        model = Valoracion
        fields = '__all__'
        widgets = {'monumento': forms.HiddenInput, 'usuario': forms.HiddenInput}

    def __init__(self, *args, **kwargs):
        super(ValoracionForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})


class FiltroForm(forms.Form):
    barrio = ModelChoiceField(queryset=None, required=False)

    def __init__(self, id, *args, **kwargs):
        super(FiltroForm, self).__init__(*args, **kwargs)
        if id:
            ciudad = get_object_or_404(Ciudad, id=id)
            self.fields['barrio'].queryset = ciudad.barrio_set.all()

