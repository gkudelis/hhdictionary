from django.db import models



class Phrase(models.CharField):
    def __init__(self, *args, **kwargs):
        super(Phrase, self).__init__(max_length=50, blank=True, *args, **kwargs)


class Phrases(models.Model):
    hello = Phrase(verbose_name='hello')
    goodBye = Phrase(verbose_name='good bye')
    yes = Phrase(verbose_name='yes')
    no = Phrase(verbose_name='no')
    whereAreYouGoing = Phrase(verbose_name='where are you going?')
    iAmGoingTo = Phrase(verbose_name='i am going to')
    here = Phrase(verbose_name='here')
    iDoNotUnderstand = Phrase(verbose_name='i do not understand')
    iAmHitchhiking = Phrase(verbose_name='i am hitchhiking')
    couldYouPickMeUp = Phrase(verbose_name='could you pick me up?')
    good = Phrase(verbose_name='good')
    bad = Phrase(verbose_name='bad')
    thankYou = Phrase(verbose_name='thank you')
    please = Phrase(verbose_name='please')
    excuseMe = Phrase(verbose_name='excuse me')
    beer = Phrase(verbose_name='beer')

    phraseList = ('hello', 'goodBye', 'yes', 'no', 'whereAreYouGoing',
                    'iAmGoingTo', 'here', 'iDoNotUnderstand', 'iAmHitchhiking',
                    'couldYouPickMeUp', 'good', 'bad', 'thankYou', 'please',
                    'excuseMe', 'beer',)

    def __unicode__(self):
        return self.language.name + u' phrases'


class Record(models.FileField):
    def __init__(self, *args, **kwargs):
        super(Record, self).__init__(upload_to=Record.uploadTo, blank=True, *args, **kwargs)

    @staticmethod
    def uploadTo(instance, filename):
        import time
        return ''.join(['records/', time.strftime('%Y-%m-%d_%H:%M:%S_'), filename])


class Records(models.Model):
    hello = Record(verbose_name='hello')
    goodBye = Record(verbose_name='good bye')
    yes = Record(verbose_name='yes')
    no = Record(verbose_name='no')
    whereAreYouGoing = Record(verbose_name='where are you going?')
    iAmGoingTo = Record(verbose_name='i am going to')
    here = Record(verbose_name='here')
    iDoNotUnderstand = Record(verbose_name='i do not understand')
    iAmHitchhiking = Record(verbose_name='i am hitchhiking')
    couldYouPickMeUp = Record(verbose_name='could you pick me up?')
    good = Record(verbose_name='good')
    bad = Record(verbose_name='bad')
    thankYou = Record(verbose_name='thank you')
    please = Record(verbose_name='please')
    excuseMe = Record(verbose_name='excuse me')
    beer = Record(verbose_name='beer')
    
    recordList = ('hello', 'goodBye', 'yes', 'no', 'whereAreYouGoing',
                    'iAmGoingTo', 'here', 'iDoNotUnderstand', 'iAmHitchhiking',
                    'couldYouPickMeUp', 'good', 'bad', 'thankYou', 'please',
                    'excuseMe', 'beer',)

    def __unicode__(self):
        return self.language.name + u' records'


class Language(models.Model):
    name = models.CharField(max_length=20, primary_key=True)
    enabled = models.BooleanField(default = False)
    phrases = models.OneToOneField(Phrases)
    records = models.OneToOneField(Records)

    def __unicode__(self):
        return self.name + u' language'
