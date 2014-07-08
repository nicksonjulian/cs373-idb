from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'cs373_Sochi.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^home/', include('home.urls')),
    url(r'^athlete/', include('athlete.urls')),
    url(r'^country/', include('country.urls')),
    url(r'^event/', include('event.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
