from django.shortcuts import render
from blogApp.models import *
# Create your views here.
def blog(request):
    
    blogs=post.objects.all()#esto es para que nos muestre todos los post
    return render(request, "blog/blog.html",{'blogs':blogs})#esto ultimo es para pasar los datos al html

def categorias_v(request, categoria_id):#se le pasa como parametro el id de la categoria en la bbdds
    categoriaa=categoria.objects.get(id=categoria_id)#esto  y la linea siguiente nos trae filtrados los datos desde la base de datos
    blogs=post.objects.filter(categorias=categoriaa) #categorias es el nombre que recibe en el modelo
    return render(request, "blog/categoria.html",{'categoriaa':categoriaa, 'blogs':blogs})