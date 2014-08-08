from django.conf.urls import patterns, url

from sponsor import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
)
