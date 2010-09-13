def currentModule(request):
    from django.conf import settings
    from menu.models import Entry

    # Get candidates and current path
    candidates = []
    for menuEntry in Entry.objects.all():
        candidates.append({
            'name': menuEntry.name,
            'path': menuEntry.path,
        })
    path = request.path

    # Determine the best candidate
    best = {
        'name': 'default',
        'length': 0,
    }
    for candidate in candidates:
        if (candidate['path'] == path[:len(candidate['path'])] 
                and len(candidate['path']) > best['length']):
            best['name'] = candidate['name']
            best['length'] = len(candidate['path'])

    if best['length'] > 0:
        currentModule = best['name']
    else:
        currentModule = settings.DEFAULT_MODULE

    return {'currentModule': currentModule}
