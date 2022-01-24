from django.db import models
from django.db import models

class servivios (models.Model):
    titulo=models.CharField(max_length=50)
    contenido=models.CharField(max_length=20)
    imagenes=models.ImageField(upload_to='mediaServicios')# en caso de necesitar imagenes se debe registrar el settings (carpeta media en la raiz)
    #i despues se registra en las urls
    create=models.DateField(auto_now_add=True)
    update=models.DateField(auto_now_add=True)#obtener la fechaactual cuando se modifica
    class Meta:
        verbose_name = 'servicio'
        verbose_name_plural ='servicios'
        
        def __str__(self):
            return self.titulo

# Create your models here.
