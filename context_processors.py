def mediaUrl(resources):
    from django.conf import settings
    return {'MEDIA_URL': settings.MEDIA_URL}
