from django.conf.urls import patterns, include, url
from django.views.generic import RedirectView
from django.contrib import admin
admin.autodiscover()
from api import AthleteResource, CountryResource, EventResource

athlete_resource = ArticleResource()
country_resource = CountryResource()
event_resource = EventResource()

urlpatterns = patterns('',
    url(r'^$', RedirectView.as_view(url='/home/')),
    url(r'^home/', include('home.urls')),
    url(r'^athlete/', include('athlete.urls')),
    url(r'^country/', include('country.urls')),
    url(r'^event/', include('event.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(athlete_resource.urls)),
    url(r'^api/', include(country_resource.urls)),
    url(r'^api/', include(event_resource.urls))
)
