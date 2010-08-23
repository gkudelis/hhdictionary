from django.conf.urls.defaults import *

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^dictionary/', 'hhdictionary.dictionary.views.dictionary'),
    (r'^admin/(.*)', admin.site.root),
)
