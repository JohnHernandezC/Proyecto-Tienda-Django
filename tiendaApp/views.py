from django.shortcuts import render
from tiendaApp.models import *

# Create your views here.
def tienda(request):
    products=producto.objects.all()#esto es para que nos muestre todos los post
    return render(request, "tienda/tienda.html",{'productos':products})#esto es para pasar el diccionario

