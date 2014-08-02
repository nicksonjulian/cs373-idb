from django.conf.urls import patterns, url
from django.contrib import admin
admin.autodiscover()
from api import api

urlpatterns = patterns('',
    #API
    url(r'^athlete/$', api.AthleteList.as_view()),
    url(r'^athlete/(?P<pk>\d+)/$', api.AthleteDetail.as_view()),
    url(r'^athlete/(?P<pk>\w+)/$', api.AthleteDetail.as_view()),

    url(r'^country/$', api.CountryList.as_view()),
    url(r'^country/(?P<pk>\w+)/$', api.CountryDetail.as_view()),
    url(r'^country/(?P<pk>\d+)/$', api.CountryDetail.as_view()),

    url(r'^event/$', api.EventsList.as_view()),
    url(r'^event/(?P<pk>\d+)/$', api.EventsDetailPK.as_view()),
    url(r'^event/(?P<sport_name>\w+)-(?P<event_name>\w+)/$', api.EventsDetail.as_view())

)
