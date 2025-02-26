from django.urls import path
from .views import registration,LoginView, LogoutView

urlpatterns = [
    path('login', LoginView, name='login'),
    path('registration', registration, name='register'),
    path('logout', LogoutView, name='logout')
]
