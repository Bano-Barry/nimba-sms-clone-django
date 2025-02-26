from django import forms
from django.contrib.auth.models import User
from sms.models import SentSms

class SentSMSForm(forms.ModelForm): 
    recipient = forms.ModelChoiceField(
        queryset=User.objects.all(),
        label="Destinataire",
        widget=forms.Select(attrs={'class': 'form-control'}),
        required=True
    )
    message = forms.CharField(
        label="Message",
        widget=forms.Textarea(attrs={'class': 'form-control'}),
        required=True
    )

    class Meta:
        model = SentSms
        fields = ['recipient', 'message']
