from django.urls import path
from .views import home, subscribe_sms_pack, tarif, user_sms_pack, user_sent_sms, user_sms_history

urlpatterns = [
    path('', home, name='home'),
    path('nos-tarifs', tarif, name='tarifs'), 
    path('subscribe/<int:pack_id>/', subscribe_sms_pack, name='subscribe_sms_pack'),
    path('mon-pack/', user_sms_pack, name='user_sms_pack'),  # Afficher le pack SMS de l'utilisateur
    path('sent-sms/', user_sent_sms, name='user_sent_sms'), # Envoyer un sms a un utilisateur du system 
    path('history', user_sms_history, name='history_sms')
]
