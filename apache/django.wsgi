import os
import sys

sys.path.append( '/var/django/giedrius' )
os.environ['DJANGO_SETTINGS_MODULE'] = 'hhdictionary.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
