from django.shortcuts import render

from sms.models import Tarif

def home(request) : 
    return render(request, 'sms/home.html')

# vue tarifs
def tarif(request) :
    tarifs =  Tarif.objects.all(); 
    return render(request, 'sms/tarif.html', context={'tarifs' : tarifs})