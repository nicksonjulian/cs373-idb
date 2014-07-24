from django.conf.urls import patterns, url

from event import views


urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^(?P<sport_name>\w+)-(?P<event_name>\w+)/$', views.detail, name='detail'),
)
