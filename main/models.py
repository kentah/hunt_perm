from django.db import models

from has.models import TimeStampedModel


class Services(TimeStampedModel):
    title = models.CharField(max_length=200)
    description = models.TextField()

    class Meta:
        verbose_name = 'Services'
        verbose_name_plural = 'Services'

    def __string__(self):
        return self.title


class Histories(TimeStampedModel):
    title = models.CharField(max_length=200)
    description = models.TextField()

    class Meta:
        verbose_name = 'Histories'
        verbose_name_plural = 'Histories'

    def __str__(self):
        return self.title


#class Images(TimeStampedModel):
#    image = ImageField()
