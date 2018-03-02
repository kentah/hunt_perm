from django.db import models

from has.models import TimeStampedModel


class Services(TimeStampedModel):
    title = models.CharField(max_length=200)
    description = models.TextField()
    #img = ForeignKey(Images)

class Histories(TimeStampedModel):
    title = models.CharField(max_length=200)
    description = models.TextField()


#class Images(TimeStampedModel):
#    image = ImageField()
