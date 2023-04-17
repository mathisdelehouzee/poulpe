from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import TypeLicense, License,Vol , ContactUrgence, Facture, Lieu, Personne, TypePersonne, Planeur, Inscription, Flarm, Adresse, Club, Log

from django.shortcuts import render, redirect
from .forms import PiloteForm, AdresseForm, ClubForm, InscriptionForm, ContactUrgenceForm

from django.shortcuts import render
from .models import Personne, Adresse, Club, Inscription, ContactUrgence
from .forms import PiloteForm, AdresseForm, ClubForm, InscriptionForm, ContactUrgenceForm

def ajouter_pilote(request):
    print("ajouter_pilote")
    if request.method == 'POST':
        print("POST ok ")
        pilote_form = PiloteForm(request.POST)
        adresse_form = AdresseForm(request.POST)
        club_form = ClubForm(request.POST)
        inscription_form = InscriptionForm(request.POST)
        contact_urgence_form = ContactUrgenceForm(request.POST)
        #if pilote_form.is_valid() and adresse_form.is_valid() and club_form.is_valid() and inscription_form.is_valid() and contact_urgence_form.is_valid():
        if pilote_form.is_valid() :
            print("is_valid ok ")
            pilote = pilote_form.save()
            adresse = adresse_form.save(commit=False)
            adresse.personne = pilote
            adresse.save()
            club = club_form.save()
            inscription = inscription_form.save(commit=False)
            inscription.pilote = pilote
            inscription.club = club
            inscription.save()
            contact_urgence = contact_urgence_form.save(commit=False)
            contact_urgence.pilote = pilote
            contact_urgence.save()
            return render(request, 'afficher_pilote.html', {'pilote': pilote})
    else:
        pilote_form = PiloteForm()
        adresse_form = AdresseForm()
        club_form = ClubForm()
        inscription_form = InscriptionForm()
        contact_urgence_form = ContactUrgenceForm()
    return render(request, 'ajouter_pilote.html', {
        'pilote_form': pilote_form,
        'adresse_form': adresse_form,
        'club_form': club_form,
        'inscription_form': inscription_form,
        'contact_urgence_form': contact_urgence_form,
    })

def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_personnes = Personne.objects.all().count()
    num_vols = Vol.objects.all().count()
    num_planeurs = Planeur.objects.all().count()

    # Available books (status = 'a')
   #rajouter si nécessaire
    # The 'all()' is implied by default.
 #   num_authors = Author.objects.count()

    context = {
        'num_personnes': num_personnes,
        'num_vols': num_vols,
        'num_planeurs': num_planeurs,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)
