from collections import namedtuple
from django.db import models


Meta = namedtuple('Meta', ['verbose_name', 'verbose_name_plural', 'ordering'])


class Tag(models.Model):
    name = models.CharField(max_length=100)


class NewsEntry(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    publish = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    tags = models.ManyToManyField(Tag, blank=True)

    meta = Meta('News Entry', 'News Entries', ['-created'])

    def __str__(self):
        return self.title
