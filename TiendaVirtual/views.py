from django.shortcuts import render,HttpResponse #se importa esto
#hay que registrar la aplicacion en serrings



def home(request):
    
    return render(request, "TiendaVirtualApp/home.html")







