from django.contrib import admin
from .models import * # importa los modelos 
# Register your models here.

class categoriaAdmin(admin.ModelAdmin):
    readonly_fields=('create','update')

class postAdmin(admin.ModelAdmin):
    readonly_fields=('create','update')
    
    
admin.site.register(categoria, categoriaAdmin)
admin.site.register(post, postAdmin)