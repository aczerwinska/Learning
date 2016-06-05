from django.conf.urls import patterns, url

from shops import views

urlpatterns = [
    url(r'^$', views.ShopList.as_view(), name='shop_list'),
    url(r'^new$', views.ShopCreate.as_view(), name='shop_new'),
    url(r'^edit/(?P<pk>\d+)$', views.ShopUpdate.as_view(), name='shop_edit'),
    url(r'^delete/(?P<pk>\d+)$', views.ShopDelete.as_view(), name='shop_delete'),

    url(r'^provider/', views.ProviderList.as_view(), name='provider_list'),
    url(r'^providerNew$', views.ProviderCreate.as_view(), name='provider_new'),
    url(r'^providerEdit/(?P<pk>\d+)$', views.ProviderUpdate.as_view(), name='provider_edit'),
    url(r'^providerDelete/(?P<pk>\d+)$', views.ProviderDelete.as_view(), name='provider_delete'),
]