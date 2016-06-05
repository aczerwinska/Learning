from __future__ import unicode_literals
from datetime import datetime
from django.db import models
from django.core.urlresolvers import reverse


# Create your models here.

class Punkt(models.Model):
    name = models.CharField(max_length=80)
    owner = models.CharField(max_length=30)
    address = models.CharField(max_length=200)
    phone = models.IntegerField()

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('punkt_edit', kwargs={'pk': self.pk})


class Herbata(models.Model):
    name = models.CharField(max_length=30)
    product = models.CharField(max_length=50)
    date = models.DateField(default=datetime.now, blank=True)
    punkt = models.ForeignKey(Punkt, on_delete=models.CASCADE)

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('herbata_edit', kwargs={'pk': self.pk})
