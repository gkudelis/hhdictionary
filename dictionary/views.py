from django.shortcuts import render_to_response
from django.template import RequestContext
from dictionary.models import Language, Phrases, Records

from django.utils.datastructures import MultiValueDictKeyError
from django.core.exceptions import ObjectDoesNotExist


def dictionary(request):
    try:
        fromLanguageName = request.GET['fromLanguage']
        toLanguageName = request.GET['toLanguage']
       
        fromLanguage = Language.objects.get(name = fromLanguageName)
        toLanguage = Language.objects.get(name = toLanguageName)
    
    except (MultiValueDictKeyError, ObjectDoesNotExist):
        #this happens when accessing the main page :)
        return render_to_response('dictionaryForm.html', {
            'languages': Language.objects.filter(enabled = True),
        }, context_instance = RequestContext(request))

    else:
        # Get phrases
        fromPhrases = fromLanguage.phrases
        toPhrases = toLanguage.phrases
     
        # Get records
        records = toLanguage.records
     
        translations = ()
        for field in Phrases.phraseList:
            translations += ({
                'fromPhrase': fromPhrases.__dict__[field],
                'toPhrase': toPhrases.__dict__[field],
                # This for some bizzare reason gives the url relative to media
                'recordUrl': records.__dict__[field],
            },)
        
        return render_to_response('dictionary.html', {
            'languages': Language.objects.filter(enabled = True),
            'translations': translations,
            'fromLanguageName': fromLanguageName,
            'toLanguageName': toLanguageName,
        }, context_instance = RequestContext(request))
