from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from sms.forms import SentSMSForm
from sms.models import SentSms, SmsPack, Tarif, UserSmsPack
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

@login_required
def user_sent_sms(request):
    if request.method == "POST":
        form = SentSMSForm(request.POST)
        if form.is_valid():
            sms = form.save(commit=False)  # Ne pas encore sauvegarder en base
            sms.user = request.user  # Associer l'utilisateur connecté
            sms.status = 'sent'  # Supposons que le SMS est envoyé avec succès
            sms.save()  # Sauvegarde en base
            
            # Récupérer le pack actif de l'utilisateur
            user_pack = UserSmsPack.objects.filter(user=request.user).first()
            
            if user_pack and user_pack.remaining_sms > 0:
                # Décrémenter le nombre de SMS restants
                user_pack.remaining_sms -= 1
                user_pack.save()
                messages.success(request, "Le SMS a été envoyé avec succès !")
            else:
                # Si l'utilisateur n'a plus de SMS restants, afficher un message d'erreur
                messages.error(request, "Vous n'avez plus de SMS restants !")
                return redirect('user_sent_sms')  # Rediriger l'utilisateur en cas d'erreur
            
            return redirect('user_sent_sms')  # Recharger la page après soumission
    else:
        form = SentSMSForm()

    return render(request, 'sms/user_sent_sms.html', {'form': form})


@login_required
def user_sms_history(request):
    """Affiche l'historique des SMS envoyés et le nombre de SMS restants."""
    sent_sms_list = SentSms.objects.filter(user=request.user).order_by('-sent_at')  # Récupérer les SMS envoyés
    user_packs = UserSmsPack.objects.filter(user=request.user)  # Récupérer les packs actifs

    return render(request, 'sms/user_history_sms.html', {
        'sent_sms_list': sent_sms_list,
        'user_packs': user_packs
    })
