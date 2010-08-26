from django.db import models



class Entry(models.Model):
    place = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)
    title = models.CharField(max_length=20)
    targetView = models.CharField(max_length=50)

    def __unicode__(self):
        return self.title
