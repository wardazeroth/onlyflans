from django.urls import path
from main.views import  acerca, indice, bienvenido, contact_form

urlpatterns = [
    path('', indice, name='indice'),
    path('acerca', acerca, name='acerca'),
    path('bienvenido', bienvenido, name='bienvenido'),
    path('contact_form', contact_form, name='contact_form')
    
]
