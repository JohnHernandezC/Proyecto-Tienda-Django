from django.shortcuts import render
from contactoApp.models import *
from .forms import formularioContacto

# Create your views here.
def contactos(request):
    formulario_contacto=formularioContacto
    return render(request, "contactos/contactos.html",{'formulario':formularioContacto})