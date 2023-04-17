from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('ajouter-pilote/', views.ajouter_pilote, name='ajouter_pilote'),
]
