from django.shortcuts import render, redirect
from app_accounts.models import *
from app_accounts.forms import *


# CVB

from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# Authentication

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

# Create your views here.

def register_request(request):

    if request.method == "POST":
        form = UserRegistrationForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            print(username)
            form.save()
            return redirect('Home')
        else:
            return render(request, 'app_blog/home.html', {"title": "Home", "message": "Anonymous", "errors": ["No pasó las validaciones"]})
    
    else:
        form = UserRegistrationForm()
        return render(request, 'app_accounts/register.html', {"form": form})

def login_request(request):

    if  request.method == "POST":

        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            data = form.cleaned_data
            username = data.get('username')
            password = data.get('password')
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                return render(request, 'app_blog/home.html', {"title": "Home", "message": f"¡Bienvenido/a {user}!"})
            else:
                return render(request, 'app_blog/home.html', {"title": "Home", "message": "Error", "errors": [f"El usuario {user} no existe"]})
        
        else:
            return render(request, 'app_blog/home.html', {"title": "Home", "message": "Anonymous", "errors": ["Revise los datos indicados"]})

    else:
        form = AuthenticationForm()
        return render(request, 'app_accounts/login.html', {"form": form})


@login_required()
def update_user(request):

    user = request.user

    if request.method == "POST":
        form = UserEditForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            user.first_name = data["first_name"]
            user.last_name = data["last_name"]
            user.email = data["email"]
            user.password1 = data["password1"]
            user.password2 = data["password2"]
            user.red_social = data["red_social"]
            user.save()
            return redirect("Home")
        else:
            form = UserEditForm(initial={"email":user.email})
            return render(request, 'app_accounts/update_user.html', {"title": "Editar usuario", "message": "Editar usuario", "form": form, "errors": ["Datos inválidos"]})
    
    else:
        form = UserEditForm(initial={"email":user.email})
        return render(request, 'app_accounts/update_user.html', {"title": "Editar usuario", "message": "Editar usuario", "form": form})

@login_required()
def profile(request):

    avatar = Avatar.objects.filter(user=request.user)

    if len(avatar) > 0:
        imagen = avatar[0].imagen.url
        return render(request, 'app_accounts/profile.html', {"image_url": imagen})

    return render (request, 'app_accounts/profile.html')

@login_required()
def upload_avatar(request):   
    
    
    if request.method == "POST":

        formulario = AvatarForm(request.POST,request.FILES)

        if formulario.is_valid():

            usuario = request.user

            avatar = Avatar.objects.filter(user=usuario)

            if len(avatar) > 0:
                avatar = avatar[0]
                avatar.imagen = formulario.cleaned_data["imagen"]
                avatar.save()

            else:
                avatar = Avatar(user=usuario, imagen=formulario.cleaned_data["imagen"])
                avatar.save()
            
        return redirect("Home")
    else:

        formulario = AvatarForm()
        return render(request, "app_accounts/upload_avatar.html", {"title": "Cargar avatar", "message": "Cargar avatar","form": formulario})
