
from django.views.generic import View
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
class inicioSessions(View):
     def get(self, request): #gestionaa y renderisa el formulario
         form=UserCreationForm()
         return render(request,"registro/registro.html",{'form':form})
     def post(self, request):#enviar los datos a la base de datos
         pass
    
