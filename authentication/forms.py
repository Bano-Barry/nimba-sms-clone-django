from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    username = forms.CharField(max_length=30, required=True, label="Nom d'utilisateur", widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'class':'form-control'}), required=True)
    password1 = forms.CharField(label="Mot de passe", max_length=30, widget=forms.TextInput(attrs={'class':'form-control', 'type': 'password'}), required=True)
    password2 = forms.CharField(label="Confirmer votre mot de passe", max_length=30, widget=forms.TextInput(attrs={'class':'form-control', 'type': 'password'}), required=True)

    class Meta:
        model = User
        fields = ["first_name","last_name","username", "email", "password1","password2"]
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'})
        }


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), label="Nom d'utilisateur", required=True, max_length=30)
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}), required=True)
