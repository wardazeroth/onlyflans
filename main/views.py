from django.http import HttpResponse
from django.shortcuts import render, redirect
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
        'cliente': 'Elmo Lesto'
    }
    return render(req, 'welcome.html', context)

def contact_form(req):
    errores = []
    customer_name = req.POST['customer_name']
    customer_email = req.POST['customer_email']
    message = req.POST['message']
    
    if len(customer_name) > 64:
        errores.append('Su nombre excede el máximo permitido')     
        
    if not '@' in customer_email:
        errores.append('Coloca @ en tu email')
        
    context = {'mensaje_error': errores}
                       
    if len(errores) > 0:
        return render(req, 'welcome.html', context)
    else:
        return render(req, 'yeah.html', context)
      
    
    
    #Ahora tengo que validar que customer_email tenga al menos 1 arroba y que customer_name  sea de largo maximo 64
    
    #si len(errores) == 0: redirijo a pagina de exito
    #si len(errores) > 0: vuelvo a cargar 'welcome.html' pero ahora mostrando los errores. 
    
