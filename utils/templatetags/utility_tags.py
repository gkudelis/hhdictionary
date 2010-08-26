from django.template import Library
from django.core.urlresolvers import reverse

register = Library()



def url_string(viewName):
    try:
        return reverse(viewName)
    except:
        return ''

register.simple_tag(url_string)
