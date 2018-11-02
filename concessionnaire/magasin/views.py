from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from fnmatch import filter
from magasin.models import Voiture


# Create your views here.
class VoitureCreate(CreateView):
    model = Voiture
    fields = '__all__'

class VoitureUpdate(UpdateView):
    model = Voiture
    fields = '__all__'

class VoitureDelete(DeleteView):
    model = Voiture
    fields = '__all__'
    #http_method_names = ['POST']
    success_url = reverse_lazy('magasin:index')

class VoitureDetail(DetailView):
    model = Voiture
    fields = '__all__'

class VoitureList(ListView):
    model = Voiture
    context_object_name = 'voiture_list'
    fields = '__all__'
    def get_queryset(self):
        return Voiture.objects.all()