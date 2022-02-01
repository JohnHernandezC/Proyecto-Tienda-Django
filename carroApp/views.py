from django.shortcuts import render
from .carro import Carro
from tiendaApp.models import producto
from django.shortcuts import redirect

# Create your views here.
def agregar_producto(request, producto_id):
    carros=Carro (request)
    productos=producto.objects.get(id=producto_id)
    carros.agregar(producto=productos)
    return redirect("Tienda")

def eliminar_producto(request, producto_id):
    carros=Carro (request)
    productos=producto.objects.get(id=producto_id)
    carros.eliminacion(producto=productos)
    return redirect("Tienda")
def restar_producto(request, producto_id):
    carros=Carro (request)
    productos=producto.objects.get(id=producto_id)
    carros.restar_unidades(producto=productos)
    return redirect("Tienda")

def limpiar_producto(request, producto_id):
    carros=Carro (request)
    carros.limpiarCarro()
    return redirect("Tienda")
