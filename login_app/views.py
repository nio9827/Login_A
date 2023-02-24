from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
# Create your views here.
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User # importamos el modelo de usuario de la base de datos 
from django.db import IntegrityError # importamos la excepcion de error de integridad

def home(request):

    mostrar = User.objects.all()

    return render(request, 'home.html', {'mostrar': mostrar})


def logiarse(request):

    if request.method == "GET":  # si el metodo es GET
        # renderizamos la pagina login.html con el formulario de autenticacion
        return render(request, "login.html", {'form': AuthenticationForm})

    else:
        # autenticamos al usuario
        user = authenticate(request, username=request.POST['username'], password=request.POST['password']) # autenticamos al usuario

       
        if user is None: # si el usuario no existe
            return render(request, "login.html", {'form': AuthenticationForm, 'error': 'Usuario no encontrado.'})
        else:
            login(request, user)
            return redirect('success')


def registrar (request):

    if request.method == "GET":  # si el metodo es GET

        return render(request, "registro.html", {'userform': UserCreationForm})
    
    else:
        if request.POST['password1'] == request.POST['password2']: 
            try:
                
                user = User.objects.create_user(username=request.POST['username'],  # creamos el usuario
                                                password=request.POST['password1'])
                print ('paso')
                user.save()  # guardamos el usuario
                 
                # redireccionamos a la pagina tarea.html
                return redirect('home')

            except IntegrityError:  # si el usuario ya existe en la base de datos

                # renderizamos la pagina registro.html con el formulario de creacion de usuarios y el error de usuario ya existente
                return render(request, "registro.html", {'userform': UserCreationForm, 'error': 'El usuario ya existe'})
    
        return render(request, 'registro.html', {'userform': UserCreationForm, 'error': 'Las contraseñas no coinciden'})
    

def success(request):
    return render(request, 'success.html')

def logout_view(request):
    logout(request)
    return redirect('home')

