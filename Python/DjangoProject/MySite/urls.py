from django.conf.urls import url
from . import views

urlpatterns = [
    # ex: /mysite/
    url(r'^$', views.index, name='index'),
    # ex: /mysite/5/
    url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    # ex: /mysite/5/results/
    url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    # ex: /mysite/5/vote/
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]
