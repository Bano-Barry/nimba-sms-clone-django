from django.db import models 
from django.contrib.auth.models import User

# Modèle représentant un pack de SMS
class SmsPack(models.Model):
    name = models.CharField(max_length=255)  # Nom du pack (ex : pack de 100 SMS)
    sms_count = models.IntegerField()  # Nombre de SMS dans ce pack
    created_at = models.DateTimeField(auto_now_add=True)  # Date et heure de création du pack

    def __str__(self):
        return self.name  # Affiche le nom du pack comme représentation textuelle

# Modèle représentant un tarif associé à un pack de SMS
class Tarif(models.Model):
    sms_pack = models.ForeignKey(SmsPack, on_delete=models.CASCADE)  # Pack de SMS auquel le tarif est associé
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Prix du pack, avec une précision de 2 décimales
    min_quantity = models.IntegerField()  # Quantité minimale de SMS pour que le tarif s'applique
    max_quantity = models.IntegerField()  # Quantité maximale de SMS pour que le tarif s'applique
    created_at = models.DateTimeField(auto_now_add=True)  # Date et heure de création du tarif

    def __str__(self):
        return f"Tarif for {self.sms_pack.name}"  # Représentation textuelle du tarif, incluant le nom du pack

# Modèle représentant l'achat d'un pack de SMS par un utilisateur
class UserSmsPack(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Utilisateur ayant acheté le pack
    sms_pack = models.ForeignKey(SmsPack, on_delete=models.CASCADE)  # Pack de SMS acheté
    remaining_sms = models.IntegerField()  # Nombre de SMS restant dans ce pack
    purchased_at = models.DateTimeField(auto_now_add=True)  # Date et heure d'achat du pack

# Modèle représentant un SMS envoyé par un utilisateur
class SentSms(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Utilisateur qui a envoyé le SMS
    recipient = models.CharField(max_length=20)  # Numéro de téléphone du destinataire
    message = models.TextField()  # Contenu du message envoyé
    sent_at = models.DateTimeField(auto_now_add=True)  # Date et heure d'envoi du SMS
    status = models.CharField(max_length=10, choices=[('sent', 'Sent'), ('failed', 'Failed')])  # Statut d'envoi du SMS (envoyé ou échoué)

    def __str__(self):
        return f"SMS to {self.recipient} by {self.user.username}"  # Représentation textuelle du SMS, indiquant le destinataire et l'utilisateur
