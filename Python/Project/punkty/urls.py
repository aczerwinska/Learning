from django.conf.urls import url

from punkty import views

urlpatterns = [
    url(r'^$', views.PunktList.as_view(), name='punkt_list'),
    url(r'^new$', views.PunktCreate.as_view(), name='punkt_new'),
    url(r'^edit/(?P<pk>\d+)$', views.PunktUpdate.as_view(), name='punkt_edit'),
    url(r'^delete/(?P<pk>\d+)$', views.PunktDelete.as_view(), name='punkt_delete'),

    url(r'^herbata/', views.HerbataList.as_view(), name='herbata_list'),
    url(r'^herbataNew$', views.HerbataCreate.as_view(), name='herbata_new'),
    url(r'^herbataEdit/(?P<pk>\d+)$', views.HerbataUpdate.as_view(), name='herbata_edit'),
    url(r'^herbataDelete/(?P<pk>\d+)$', views.HerbataDelete.as_view(), name='herbata_delete'),
]