from django.contrib import admin

# Register your models here.
from Encodage_pilote.models import TypeLicense, License,Vol , ContactUrgence, Facture, Lieu, Personne, TypePersonne, Planeur, Inscription, Flarm, Adresse, Club, Log

admin.site.register(License)
admin.site.register(Vol)
admin.site.register(ContactUrgence)
admin.site.register(Facture)
admin.site.register(Flarm)
admin.site.register(Log)
admin.site.register(Lieu)
admin.site.register(Planeur)
admin.site.register(Personne)
admin.site.register(TypePersonne)
admin.site.register(Inscription)
admin.site.register(Adresse)
admin.site.register(Club)
admin.site.register(TypeLicense)
