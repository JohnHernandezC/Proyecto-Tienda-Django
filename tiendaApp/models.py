from django.db import models


class categoriaProducto (models.Model):
    nombre=models.CharField(max_length=50)
    create=models.DateField(auto_now_add=True)
    update=models.DateField(auto_now=True)
    class Meta:
        verbose_name = 'categoriap'
        verbose_name_plural ='categoriasp'
        
    def __str__(self):
        return self.nombre
    
class producto (models.Model):
    nombrep=models.CharField(max_length=50)
    categoria=models.ForeignKey(categoriaProducto, on_delete=models.CASCADE)#el ondelete es para borrar en cascada junto a la lave foranea
    imagen=models.ImageField(upload_to='mediaTienda', null=True, blank=True)
    precio=models.FloatField()
    disponibilidad=models.BooleanField(default=True)
    create=models.DateField(auto_now_add=True)
    update=models.DateField(auto_now=True)
    class Meta:
        verbose_name = 'producto'
        verbose_name_plural ='productos'
        
    def __str__(self):
        return self.nombrep

