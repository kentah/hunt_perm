from django.conf import settings
from django.db import models

from has.models import TimeStampedModel


class Category(TimeStampedModel):
    title = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, db_index=True)

    class Meta:
        verbose_name_plural = 'Categories'

    def __string__(self):
        return self.title


class Post(TimeStampedModel):
    '''
    author = models.ForeignKey(
    settings.AUTH_USER_MODEL,
    on_delete= models.CASCADE
    )
    '''
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    body = models.TextField()
    category = models.ForeignKey(Category, verbose_name='Category', on_delete=models.PROTECT)

    def __string__(self):
        return self.title
