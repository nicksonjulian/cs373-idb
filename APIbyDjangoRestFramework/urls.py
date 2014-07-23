from django.conf.urls import patterns, include, url
from django.views.generic import RedirectView
from django.contrib import admin
admin.autodiscover()
from rest_framework.url patterns import format_suffix_patterns
from  import api

urlpatterns = patterns('',
    url(r'^$', RedirectView.as_view(url='/home/')),
    url(r'^home/', include('home.urls')),
    url(r'^athlete/', include('athlete.urls')),
    url(r'^country/', include('country.urls')),
    url(r'^event/', include('event.urls')),
    url(r'^admin/', include(admin.site.urls)),

    #API
    url(r'^api/athlete/$', api.AthleteList.as_view()),
    url(r'^api/athlete/(?P<pk>[0-9]+)/$', api.AthleteDetail.as_view()),

    url(r'^api/country/$', api.CountryList.as_view()),
    url(r'^api/country/(?P<pk>[0-9]+)/$', api.CountryDetail.as_view())

    url(r'^api/event/$', api.EventList.as_view()),
    url(r'^api/event/(?P<pk>[0-9]+)/$', api.EventDetail.as_view())

)
