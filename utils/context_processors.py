def mediaUrl(request):
    from django.conf import settings
    return {'MEDIA_URL': settings.MEDIA_URL}

def currentPath(request):
    return {'currentPath': request.path}
