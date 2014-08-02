from django.conf.urls import patterns, include, url
from django.views.generic import RedirectView
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', RedirectView.as_view(url='/home/')),
    url(r'^home/', include('home.urls')),
    url(r'^athlete/', include('athlete.urls')),
    url(r'^country/', include('country.urls')),
    url(r'^event/', include('event.urls')),
    url(r'^api/', include('api.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
