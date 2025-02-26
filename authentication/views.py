from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout # import des fonctions login et authenticate

from .forms import RegisterForm, LoginForm


def registration(request): 
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            raise ValueError('le formulaire n\'est pas valide ')
    form = RegisterForm()
    return render(request=request, template_name='authentication/registration.html', context= {'form':form})

# def LoginView(request):
#     form = LoginForm()
    
#     if request.method == 'POST':
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             myform = form.cleaned_data
#             username = myform['username']
#             password = myform['username']
#             user = authenticate(request=request, username= username, password = password)
#             if user is not None:
#                 login(request , user)
#         else:
#             print('pas valide')
#     return render(request=request, template_name='authentication/login.html', context={'form':form})    

def LoginView(request):
    form = LoginForm(data=request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                messages.success(request, "Connexion réussie !")
                return redirect('home')  # Redirection après connexion
            else:
                print('pas valide')
                messages.error(request, "Nom d'utilisateur ou mot de passe incorrect.")

    return render(request, 'authentication/login.html', {'form': form})

def LogoutView(request):
    logout(request)
    messages.success(request, "Vous avez été déconnecté avec succès.")
    return redirect('home')  # Redirige vers la page d'accueil après déconnexion
