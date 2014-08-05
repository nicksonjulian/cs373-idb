from django.conf.urls import patterns, url
from django.contrib import admin
admin.autodiscover()
from api import api
import haystack
haystack.autodiscover()

urlpatterns = patterns('',
    url(r'^search/', include('haystack.urls'))

)
