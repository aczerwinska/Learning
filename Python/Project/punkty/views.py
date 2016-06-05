from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from punkty.models import Punkt, Herbata


# Create your views here.

class PunktList(ListView):
    model = Punkt


class PunktCreate(CreateView):
    model = Punkt
    success_url = reverse_lazy('punkt_list')
    fields = ['name', 'owner', 'address', 'phone']


class PunktUpdate(UpdateView):
    model = Punkt
    success_url = reverse_lazy('punkt_list')
    fields = ['name', 'owner', 'address', 'phone']


class PunktDelete(DeleteView):
    model = Punkt
    success_url = reverse_lazy('punkt_list')


class HerbataList(ListView):
    model = Herbata


class HerbataCreate(CreateView):
    model = Herbata
    success_url = reverse_lazy('herbata_list')
    fields = ['name', 'product', 'date', 'shop']


class HerbataUpdate(UpdateView):
    model = Herbata
    success_url = reverse_lazy('herbata_list')
    fields = ['name', 'product', 'date', 'shop']


class HerbataDelete(DeleteView):
    model = Herbata
    success_url = reverse_lazy('herbata_list')
