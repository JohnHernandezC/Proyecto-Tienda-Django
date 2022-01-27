from django.urls import path
from TiendaVirtual import views
from django.conf import settings
from django.conf.urls.static import static

 #aqui agragamos la url de esta app (pueden haber varias apps)

urlpatterns = [
    
    path('', views.home, name='Home'),
    
    path('tienda/',views.tienda, name='Tienda'),
    
    
    
]
urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#esto y los imports es para la carpeta imagenes y que sea posibe visibilisarlo