from __future__ import unicode_literals
from datetime import datetime
from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.

class Shop(models.Model):
    name = models.CharField(max_length=80)
    owner = models.CharField(max_length=30)
    address = models.CharField(max_length=200)
    phone = models.IntegerField()

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop_edit', kwargs={'pk': self.pk})

class Provider(models.Model):
    name = models.CharField(max_length=30)
    product = models.CharField(max_length=50)
    contract_date = models.DateField(default=datetime.now, blank=True)
    phone = models.IntegerField()
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('provider_edit', kwargs={'pk': self.pk})