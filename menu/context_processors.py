def currentModule(request):
    from django.conf import settings
    
    # Cut off static path prefix
    cutPath = request.path[len(settings.PATH_PREFIX):]

    # Get first word ( == module )
    if len(cutPath) > 0:
        i = cutPath.find('/')
        if i == -1: #Not found
            currentModule = cutPath
        else:
            currentModule = cutPath[:i]
    else:
        currentModule = settings.DEFAULT_MODULE

    return {'currentModule': currentModule}


def pathPrefix(reqest):
    from django.conf import settings
    return {'PATH_PREFIX': settings.PATH_PREFIX}
