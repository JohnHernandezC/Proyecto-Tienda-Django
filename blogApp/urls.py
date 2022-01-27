from django.urls import path
from . import views


urlpatterns = [
    
    path('', views.blog, name='Blog'),
    path('categoria/<int:categoria_id>/', views.categorias_v, name='categoria'),
    #categoria_id es eñ parametro que recibira desde la base de datos por eso va entre corchetes
  
]