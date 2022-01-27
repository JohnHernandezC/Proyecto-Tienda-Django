from django import forms

class formularioContacto(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)
    nombre = forms.CharField(label='Nombre', max_length=100,required=True)
    email = forms.CharField(label='Email', max_length=30,required=True)
    contenido = forms.CharField(label='contenido')
    
    
    