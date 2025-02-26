from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from sms.models import SmsPack, Tarif, UserSmsPack
from django.contrib.auth.decorators import login_required
def home(request) : 
    return render(request, 'sms/home.html')

# vue tarifs
def tarif(request) :
    tarifs =  Tarif.objects.all(); 
    return render(request, 'sms/tarif.html', context={'tarifs' : tarifs})

@login_required
def subscribe_sms_pack(request, pack_id):
    """_summary_

    Vérifie si l'utilisateur est authentifié
    Récupère le pack sélectionné
    Vérifie si l'utilisateur a déjà un pack
    Ajoute ou met à jour son pack de SMS
    """
    sms_pack = get_object_or_404(SmsPack, id=pack_id)  # Récupérer le pack sélectionné
    
    # Vérifier si l'utilisateur a déjà un pack actif
    user_pack, created = UserSmsPack.objects.get_or_create(
        user=request.user,
        sms_pack=sms_pack,
        defaults={'remaining_sms': sms_pack.sms_count}  # Initialise le solde avec la quantité du pack
    )

    if not created:
        # Si l'utilisateur a déjà souscrit, ajouter les SMS au solde existant
        user_pack.remaining_sms += sms_pack.sms_count
        user_pack.save()
        messages.success(request, f"Votre pack a été mis à jour avec {sms_pack.sms_count} SMS supplémentaires !")
    else:
        messages.success(request, f"Vous avez souscrit avec succès au pack {sms_pack.name}.")

    return redirect('home')  # Redirection vers la page d'accueil après souscription

@login_required
def user_sms_pack(request):
    """Affiche les informations sur le pack SMS de l'utilisateur connecté."""
    # Récupérer le pack SMS de l'utilisateur connecté
    try:
        user_packs = UserSmsPack.objects.filter(user=request.user)
    except UserSmsPack.DoesNotExist:
        user_packs = None

    # Passer l'objet user_pack au template
    return render(request, 'sms/user_pack.html', {'user_packs': user_packs})