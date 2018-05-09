from django.db import models

from has.models import TimeStampedModel


class Services(TimeStampedModel):
    title = models.CharField(max_length=200)
    description = models.TextField()
    #img = ForeignKey(Images)

class Histories(TimeStampedModel):
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.title


#class Images(TimeStampedModel):
#    image = ImageField()
