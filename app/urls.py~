from django.conf.urls import patterns, url

from app import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^(?P<request_id>\d+)/results/$', views.results, name='results'),
    url(r'^search-form/$', views.search_form ,name='search-form'),
    url(r'^search-form/search/$', views.search),
    url(r'^contact/$', views.contact ,name='contact'),
    url(r'^create/$', views.create,name='create'),
    url(r'^create/thanks/$', views.thanks),
)

