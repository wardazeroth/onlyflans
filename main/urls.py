from django.urls import path
from main.views import  acerca, indice, bienvenido, exito

urlpatterns = [
    path('', indice, name='indice'),
    path('acerca', acerca, name='acerca'),
    path('bienvenido', bienvenido, name='bienvenido'),
    path('yeah', exito)

]
