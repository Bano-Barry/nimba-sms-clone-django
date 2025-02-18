from django.urls import path
from .views import home, tarif

urlpatterns = [
    path('', home, name='home'),
    path('nos-tarifs', tarif, name='tarifs')
]
