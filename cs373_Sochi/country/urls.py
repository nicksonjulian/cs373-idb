from django.conf.urls import patterns, url

from country import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^usa/', views.usa, name='us'),
    url(r'^germany/', views.ger, name='ger'),
    url(r'^netherlands/', views.ned, name='ned'),
    url(r'^(?P<country_id>\d+)/$', views.detail, name='detail'),
)
