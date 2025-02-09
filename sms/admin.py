from django.contrib import admin

from sms.models import SmsPack, Tarif, UserSmsPack, SentSms

# Enregistrement du modèle SmsPack dans l'administration pour gérer les packs de SMS
admin.site.register(SmsPack)

# Enregistrement du modèle Tarif dans l'administration pour gérer les tarifs associés aux packs de SMS
admin.site.register(Tarif)

# Enregistrement du modèle UserSmsPack dans l'administration pour gérer les abonnements des utilisateurs aux packs de SMS
admin.site.register(UserSmsPack)

# Enregistrement du modèle SentSms dans l'administration pour gérer l'historique des SMS envoyés par les utilisateurs
admin.site.register(SentSms)