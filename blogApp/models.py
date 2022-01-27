from django.db import models
from django.contrib.auth.models import User#para llaves foraneas

class categoria (models.Model):
    nombre=models.CharField(max_length=50)
    create=models.DateField(auto_now_add=True)
    update=models.DateField(auto_now_add=True)
    class Meta:
        verbose_name = 'categoria'
        verbose_name_plural ='categorias'
        
    def __str__(self):
        return self.nombre




class post (models.Model):
    titulo=models.CharField(max_length=50)
    contenido=models.CharField(max_length=20)
    imagenes=models.ImageField(upload_to='mediaBlogs', null=True, blank=True)# en caso de necesitar imagenes se debe registrar el settings (carpeta media en la raiz)
    autor=models.ForeignKey(User, on_delete=models.CASCADE)#para hacer una eliminacion en cascada o usar llaves foraneas (relacio 1 a varios)
    categorias=models.ManyToManyField(categoria)#para hacer una representacion muchos a muchos con la clase categoria
    create=models.DateField(auto_now_add=True)
    update=models.DateField(auto_now_add=True)#
    class Meta:
        verbose_name = 'post'
        verbose_name_plural ='posts'
        
        
    def __str__(self):
        return self.titulo