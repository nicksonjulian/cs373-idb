from django.conf.urls import patterns, url

from athlete import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^ireenwust/', views.ireen, name='ireen'),
    url(r'^tobiasarlt/', views.tobias, name='tobias'),
    #url(r'^(?P<athlete_id>\d+)/$', views.detail, name='detail'),
)
