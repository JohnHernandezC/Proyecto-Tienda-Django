from django.shortcuts import render,HttpResponse #se importa esto
#hay que registrar la aplicacion en serrings
from serviciosApp.models import servivios

# Create your views here.
def servicios(request):
    servicios=servivios.objects.all()
    return render(request, "servicios/servicios.html", {'servicios':servicios})