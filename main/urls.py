from django.urls import path
from main.views import  acerca, indice, bienvenido, exito, contacto, register

urlpatterns = [
    path('', indice, name='indice'),
    path('acerca', acerca, name='acerca'),
    path('bienvenido', bienvenido, name='bienvenido'),
    path('contact', contacto, name = 'contacto'),
    path('yeah', exito),
    # path('login', login),
    path('register', register)
]
