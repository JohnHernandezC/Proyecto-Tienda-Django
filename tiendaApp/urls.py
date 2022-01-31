from django.urls import path
from tiendaApp import views

from django.conf.urls.static import static

 #aqui agragamos la url de esta app (pueden haber varias apps)

urlpatterns = [
    
    path('',views.tienda, name='Tienda'),

]
