from django.shortcuts import render,HttpResponse #se importa esto
#hay que registrar la aplicacion en serrings



def home(request):
    
    return render(request, "TiendaVirtualApp/home.html")



def tienda(request):
    
    return render(request, "TiendaVirtualApp/tienda.html")

def blog(request):
    
    return render(request, "TiendaVirtualApp/blog.html")

def contactos(request):
    
    return render(request, "TiendaVirtualApp/contactos.html")
