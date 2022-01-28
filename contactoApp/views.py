from django.shortcuts import render, redirect
from contactoApp.models import *
from .forms import formularioContacto
from django.core.mail import EmailMessage

# Create your views here.
def contactos(request):
    formulario_contacto=formularioContacto()
    if request.method == 'POST':
        formulario_contacto=formularioContacto(data=request.POST)
        if formulario_contacto.is_valid():
            your_name=request.POST.get("your_name")
            nombre=request.POST.get("nombre")
            email=request.POST.get("email")
            contenido=request.POST.get("contenido")#obtener los datos del formulario y guardaros en una variable
            
            emails=EmailMessage("Mensaje de appDjango","El usuario {} con el correo {} escribio:\n\n{}".format(nombre,email,contenido),
                               "",[email],reply_to=[email])#lo ultimo es por si quieren colocar la opcion de responder
            try:
                emails.send()
                return redirect('/contactos/?valido')
            except:
                return redirect('/contactos/?novalido')
            
    return render(request, "contactos/contactos.html",{'formulario':formularioContacto})