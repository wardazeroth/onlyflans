from django.http import HttpResponse
from django.shortcuts import render
from main.pasteles import flanes

# Create your views here.

def indice(req):
    context = {
    'flan': flanes
    }
    return render(req, 'index.html', context)

def acerca(req):
    return render(req, 'about.html')

def bienvenido(req):
    context = {
        'cliente': 'Mente Maestra'
    }
    return render(req, 'welcome.html', context)
