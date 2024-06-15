from django import forms
from .models import Muntu

class Cible(forms.ModelForm):
    class Meta:
        model = Muntu
        fields = ['nom', 'mot_de_passe']
        password = forms.CharField(widget=forms.PasswordInput(), label='Mot de passe')
        name = forms.CharField(max_length=255, label='Nom')