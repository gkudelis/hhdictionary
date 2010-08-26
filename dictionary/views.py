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

        # Get dictionaries and NOT objects
        fromPhrases = Phrases.objects.get(language = fromLanguage)
        toPhrases = Phrases.objects.get(language = toLanguage)

        translations = ()
        for field in Phrases.phraseList:
            translations += ({
                'fromPhrase':  fromPhrases.__dict__[field],
                'toPhrase': toPhrases.__dict__[field],
            },)
        
        return render_to_response('dictionary.html', {
            'languages': Language.objects.all(),
            'translations': translations,
        }, context_instance = RequestContext(request))

    except (MultiValueDictKeyError, ObjectDoesNotExist):
        #this happens when accessing the main page :)
        return render_to_response('dictionaryForm.html', {
            'languages': Language.objects.all(),
        }, context_instance = RequestContext(request))
