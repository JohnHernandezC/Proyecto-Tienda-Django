from django.urls import path
from TiendaVirtual import views

 #aqui agragamos la url de esta app (pueden haber varias apps)

urlpatterns = [
    
    path('', views.home, name='Home'),
    path('servicios/',views.servicios, name='Servicios'),
    path('tienda/',views.tienda, name='Tienda'),
    path('blog/', views.blog, name='Blog'),
    path('contactos/', views.contactos, name='Contactos'),
    
]