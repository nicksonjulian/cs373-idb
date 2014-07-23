from django.conf.urls import patterns, url

from event import views


urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^ldoubles/', views.ldoubles, name='ldoubles'),
    url(r'^ssladies3000m/', views.ssladies3000m, name='ssladies3000m'),
    url(r'^fsicedancefreedance/', views.fsicedancefreedance, name='fsdance'),
    url(r'^(?P<event_id>\d+)/$', views.detail, name='detail'),
)
