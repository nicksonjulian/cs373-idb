from django.conf.urls import patterns, url

from athlete import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^(?P<athlete_id>\d+)/$', views.detail, name='detail'),
)
