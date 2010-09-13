from django.db import models



class Phrase(models.CharField):
    def __init__(self):
        models.CharField.__init__(self, max_length=50, blank=True)


class Phrases(models.Model):
    hello = Phrase()
    goodBye = Phrase()
    yes = Phrase()
    no = Phrase()
    whereAreYouGoing = Phrase()
    iAmGoingTo = Phrase()
    here = Phrase()
    iDoNotUnderstand = Phrase()
    iAmHitchhiking = Phrase()
    couldYouPickMeUp = Phrase()
    good = Phrase()
    bad = Phrase()
    thankYou = Phrase()
    please = Phrase()
    excuseMe = Phrase()
    beer = Phrase()

    phraseList = ('hello', 'goodBye', 'yes', 'no', 'whereAreYouGoing',
                    'iAmGoingTo', 'here', 'iDoNotUnderstand', 'iAmHitchhiking',
                    'couldYouPickMeUp', 'good', 'bad', 'thankYou', 'please',
                    'excuseMe', 'beer',)

    def __unicode__(self):
        return self.language.name + u' phrases'


class Record(models.FileField):
    def __init__(self):
        models.FileField.__init__(self, upload_to=Record.uploadTo, blank=True)

    @staticmethod
    def uploadTo(instance, filename):
        import time
        return ''.join(['records/', time.strftime('%Y-%m-%d_%H:%M:%S_'), filename])


class Records(models.Model):
    hello = Record()
    goodBye = Record()
    yes = Record()
    no = Record()
    whereAreYouGoing = Record()
    iAmGoingTo = Record()
    here = Record()
    iDoNotUnderstand = Record()
    iAmHitchhiking = Record()
    couldYouPickMeUp = Record()
    good = Record()
    bad = Record()
    thankYou = Record()
    please = Record()
    excuseMe = Record()
    beer = Record()
    
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
