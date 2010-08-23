from django.db import models



class Language(models.Model):
    name = models.CharField(max_length=20, primary_key=True)

    def __unicode__(self):
        return self.name + u' language'


class Phrase(models.CharField):
    def __init__(self):
        models.CharField.__init__(self, max_length=50)


class Phrases(models.Model):
    language = models.OneToOneField(Language)
    
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

    def uploadTo(self, filename):
        return 'records/' + self.language.name + '_' + filename


class Records(models.Model):
    language = models.OneToOneField(Language)

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
    thankYou = Phrase()
    please = Record()
    excuseMe = Record()
    beer = Record()
    
    recordList = ('hello', 'goodBye', 'yes', 'no', 'whereAreYouGoing',
                    'iAmGoingTo', 'here', 'iDoNotUnderstand', 'iAmHitchhiking',
                    'couldYouPickMeUp', 'good', 'bad', 'thankYou', 'please',
                    'excuseMe', 'beer',)

    def __unicode__(self):
        return self.language.name + u' records'


