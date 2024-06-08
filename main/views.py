from django.http import HttpResponse
from django.shortcuts import render, redirect
from main.pasteles import flanes
from main.forms import OnlyflanForm
from main.models import Persona

# Create your views here.

def indice(req):
    context = {
    'flan': flanes
    }
    return render(req, 'index.html', context)

def acerca(req):
    return render(req, 'about.html')

def bienvenido(req):  
    if req.method == 'GET':
        form = OnlyflanForm()
        context = {'form': form}
        return render(req, 'welcome.html', context)
        # renderizamos la página
    else:
        # validamos el formulario
        form = OnlyflanForm(req.POST)
        if form.is_valid():
            #esta es la forma de pedirle a un modelo que cree un registro usando los datos de un formulario
            Persona.objects.create(
                **form.cleaned_data
            )
            # Persona.objects.create({
            #     'nombre': form.nombre,
            #     'email': form.email,
            #     'mensaje': form.mensaje               
            # })
            return redirect('/yeah')
        context = {'form': form}
        return render(req, 'welcome.html', context)
    

def exito(req):
    return render(req, 'yeah.html')
    
    # cont = {
    #         'cliente': 'Elmo Lesto'
    #     }
    # return render(req, 'welcome.html', context)

# def contact_form(req):
#     errores = []
#     customer_name = req.POST['customer_name']
#     customer_email = req.POST['customer_email']
#     message = req.POST['message']
    
#     if len(customer_name) > 64:
#         errores.append('Su nombre excede el máximo permitido')     
        
#     if not '@' in customer_email:
#         errores.append('Coloca @ en tu email')
        
#     context = {'mensaje_error': errores}
                       
#     if len(errores) > 0:
#         return render(req, 'welcome.html', context)
#     else:
#         return render(req, 'yeah.html', context)

   
# def contact_form(req):
#   if req.method == 'GET':
#     form = OnlyflanForm()
#     context = {'form': form}
#     return render(req, 'welcome.html', context)
#     # renderizamos la página
#   else:
#     # validamos el formulario
#     form = OnlyflanForm(req.POST)
#     if form.is_valid():
#       return redirect('/yeah')
#     context = {'form': form}
#     return render(req, 'welcome.html', context)

  
    
    
    #Ahora tengo que validar que customer_email tenga al menos 1 arroba y que customer_name  sea de largo maximo 64
    
    #si len(errores) == 0: redirijo a pagina de exito
    #si len(errores) > 0: vuelvo a cargar 'welcome.html' pero ahora mostrando los errores. 
    
