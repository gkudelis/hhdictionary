def activeView(request):
    from django.core.urlresolvers import resolve
    from django.conf import settings
    path = request.path[len(settings.PATH_PREFIX):]
    func = resolve(path)[0]
    return {'activeView': func.__module__+'.'+func.__name__}
