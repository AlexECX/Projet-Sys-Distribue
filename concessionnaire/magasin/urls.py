"""concessionnaire URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

from magasin.views import VoitureAdd, VoitureDelete, VoitureDetail, VoitureUpdate, VoitureList, FactureList, FactureDetail, VoitureVendre

app_name = 'magasin'
urlpatterns = [
    path('', TemplateView.as_view(template_name='magasin/index.html'), name='index'),
    path('voiture/add/', VoitureAdd.as_view(), name='voiture-add'),
    path('voiture/list/', VoitureList.as_view(), name='voiture-list'),
    path('voiture/<int:pk>/', VoitureDetail.as_view(), name='voiture-detail'),
    path('voiture/<int:pk>/vendre/', VoitureVendre.as_view(), name='voiture-vendre'),
    path('voiture/<int:pk>/delete/', VoitureDelete.as_view(), name='voiture-delete'),
    path('facture/list/', FactureList.as_view(), name='facture-list'),
    path('facture/<int:pk>/', FactureDetail.as_view(), name='facture-detail'),
]