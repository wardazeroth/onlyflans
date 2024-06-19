from django.http import HttpResponse
from django.shortcuts import render, redirect
from main.pasteles import flanes
from main.forms import OnlyflanForm, RegisterForm
from main.models import Contacto, Flan
from django.contrib.auth.decorators import login_required
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.views import LoginView
from django.contrib import messages
from django.contrib.auth.models import User


# Create your views here.

class LoginViewPropia(SuccessMessageMixin, LoginView):
    success_message = 'Has ingresado correctamente'

def indice(req):
    #Debe mostrar todos los flanes
    flanes_publicos = Flan.objects.filter(is_private=False)
    context = {
    'flan': flanes_publicos
    }
    return render(req, 'index.html', context)

def acerca(req):
    return render(req, 'about.html')

def contacto(req):  
    if req.method == 'GET':
        form = OnlyflanForm()
        context = {'form': form}
        return render(req, 'contact.html', context)
        # renderizamos la página
    else:
        # validamos el formulario
        form = OnlyflanForm(req.POST)
        if form.is_valid():
            #esta es la forma de pedirle a un modelo que cree un registro usando los datos de un formulario
            Contacto.objects.create(
                **form.cleaned_data
            )
            # Persona.objects.create({
            #     'nombre': form.nombre,
            #     'email': form.email,
            #     'mensaje': form.mensaje               
            # })
            return redirect('/yeah')
        context = {'form': form}
        return render(req, 'contact.html', context)

@login_required
def bienvenido(req):
    #debe mostrar solo los flanes privados de la base de datos
    flanes_privados = Flan.objects.filter(is_private=True)
    flanes_publicos = Flan.objects.filter(is_private = False)
    flanes = Flan.objects.all()
    context = {
    'flan' : flanes
    }
    return render (req, 'welcome.html', context)

def exito(req):
    return render(req, 'yeah.html')


def register(req):
    form = RegisterForm()
    context = {'form': form}
    if req.method == 'GET':
        return render(req, 'registration/register.html', context)
    #en caso de POST
    form = RegisterForm(req.POST)
    if form.is_valid():
        data = form.cleaned_data
        if data['password'] != data['passRepeat']:
            messages.warning(req, 'Ambas contraseñas deben coincidir')
            return redirect('/accounts/register/')
        
        User.objects.create_user(data['username'], data['email'], data['password'])
        messages.success(req, '¡El usuario ha sido creado con éxito!')
    return redirect('/')


def detalleFlan(req, id):
    
    # flanes_privados = Flan.objects.filter(is_private=True)
    # flanes_publicos = Flan.objects.filter(is_private = False)
    flanes = Flan.objects.all()
    # id = int(id)
    # flanes= Flan.objects.get(id)

    id = int(id)
    flan_hallado = None
    for i in flanes:
        if i.id == id:
            flan_hallado = i
    ingredientes = flan_hallado.ingredientes.split(';')
    context = {
        'flan': flan_hallado,
        'ingredientes': ingredientes
    }
    return render (req, 'detalle.html', context)
    


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
    
