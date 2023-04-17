from django import forms
from .models import Personne, Adresse, Club, Inscription, ContactUrgence

class PiloteForm(forms.ModelForm):
    class Meta:
        model = Personne
        #fields = ['nom', 'prenom', 'date_naissance', 'lieu_naissance', 'telephone', 'gsm', 'mail', 'niss', 'ville', 'idclub', 'idinscription']
        fields = ['nom', 'prenom',  'lieu_naissance', 'telephone', 'gsm', 'mail']

        # widgets = {
        #     'date_naissance': forms.DateInput(attrs={'type': 'date'}),
        #     'ville': forms.Select(choices=Adresse.objects.all()),
        #     'idclub': forms.Select(choices=Club.objects.all()),
        #     'idinscription': forms.Select(choices=Inscription.objects.all()),
        # }

class AdresseForm(forms.ModelForm):
    class Meta:
        model = Adresse
        fields = ['ville', 'pays', 'code_postal']

class ClubForm(forms.ModelForm):
    class Meta:
        model = Club
        fields = ['nom', 'alive']

class InscriptionForm(forms.ModelForm):
    class Meta:
        model = Inscription
        fields = ['typeassurance', 'caution', 'cotisation', 'date', 'actif', 'forfait_saison', 'stage', 'fcfvv']

class ContactUrgenceForm(forms.ModelForm):
    class Meta:
        model = ContactUrgence
        fields = ['nom', 'prenom', 'telephone']
        widgets = {
            'estrelie': forms.CheckboxSelectMultiple(choices=Personne.objects.all()),
        }
