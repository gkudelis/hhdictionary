from django.conf.urls.defaults import *

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^$', 'dictionary.views.dictionary'),
    (r'^admin/(.*)', admin.site.root),
    (r'^dictionary', 'dictionary.views.dictionary'),
    (r'^news', include('news.urls')),
)
