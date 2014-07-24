from django.conf.urls import patterns, url

from country import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^(?P<country_id>\w+)/$', views.detail, name='detail'),
)
