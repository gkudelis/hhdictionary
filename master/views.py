from django.shortcuts import render_to_response
from django.template import loader, Context, RequestContext

from hhdictionary.menu.views import menu


def master(request):
    # TODO:
    # Atsirinkimas pagal URL
    # bodyclass parametras
    # sutvarkyti bodyclass CSS'e

    # Render menu
    renderedMenu = menu(request).content
