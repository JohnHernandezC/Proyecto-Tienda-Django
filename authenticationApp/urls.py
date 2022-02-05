from django.urls import path
from .views import inicioSessions




urlpatterns = [
    path('', inicioSessions.as_view(), name='Autenticacion'),
    #el asview es para que nos muestre la clase como una vista
]
