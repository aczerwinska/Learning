from django.shortcuts import render

from django.http import HttpResponse
from django.views.generic import  TemplateView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy

from shops.models import Shop, Provider

# Create your views here.

class ShopList(ListView):
    model = Shop

class ShopCreate(CreateView):
    model = Shop
    success_url = reverse_lazy('shop_list')
    fields = ['name', 'owner', 'address', 'phone']

class ShopUpdate(UpdateView):
    model = Shop
    success_url = reverse_lazy('shop_list')
    fields = ['name', 'owner', 'address', 'phone']

class ShopDelete(DeleteView):
    model = Shop
    success_url = reverse_lazy('shop_list')




class ProviderList(ListView):
    model = Provider

class ProviderCreate(CreateView):
    model = Provider
    success_url = reverse_lazy('provider_list')
    fields = ['name', 'product', 'contract_date', 'phone', 'shop']

class ProviderUpdate(UpdateView):
    model = Provider
    success_url = reverse_lazy('provider_list')
    fields = ['name', 'product', 'contract_date', 'phone', 'shop']

class ProviderDelete(DeleteView):
    model = Provider
    success_url = reverse_lazy('provider_list')