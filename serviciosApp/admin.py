from django.contrib import admin
from serviciosApp.models import servivios


class servicios_admin (admin.ModelAdmin):
    
    
    readonly_fields=("create","update")# mostrar los archivos que no se muestran por defecto

# Register your models here.
admin.site.register(servivios, servicios_admin)
