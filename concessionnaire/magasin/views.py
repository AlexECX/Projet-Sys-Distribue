from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.db.models import Q

from fnmatch import filter
from magasin.models import Voiture, Facture


# Create your views here.
class VoitureAdd(CreateView):
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
        self.queryset = Voiture.objects.filter(
            ~Q(id__in=Facture.objects.values_list('voitureVendue_id', flat=True))
        )
        return super().get_queryset()

    def get_ordering(self):
        ordering = self.request.GET.get('orderby', 'no_serie')
        return ordering


class VoitureVendre(CreateView):
    model = Facture
    fields = ['nom_acheteur', 'montant']

    def form_valid(self, form):
        form.instance.voitureVendue = Voiture.objects.get(pk=self.kwargs['pk'])
        return super().form_valid(form)


class FactureList(ListView):
    model = Facture
    context_object_name = 'facture_list'
    fields = '__all__'


class FactureDetail(DetailView):
    model = Facture
    fields = '__all__'
