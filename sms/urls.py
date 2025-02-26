from django.urls import path
from .views import home, subscribe_sms_pack, tarif, user_sms_pack

urlpatterns = [
    path('', home, name='home'),
    path('nos-tarifs', tarif, name='tarifs'), 
    path('subscribe/<int:pack_id>/', subscribe_sms_pack, name='subscribe_sms_pack'),
     path('mon-pack/', user_sms_pack, name='user_sms_pack'),  # Afficher le pack SMS de l'utilisateur
]
