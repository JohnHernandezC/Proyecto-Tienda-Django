from django.contrib import admin
from .models import * # importa los modelos 
# Register your models here.

class categoriaProAdmin(admin.ModelAdmin):
    readonly_fields=('create','update')

class productoAdmin(admin.ModelAdmin):
    readonly_fields=('create','update')
    
    
admin.site.register(categoriaProducto , categoriaProAdmin)
admin.site.register(producto, productoAdmin)