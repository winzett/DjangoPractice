from __future__ import unicode_literals

from django.db import models



# Create your models here.


class Risk_map_article(models.Model):
    hashcode = models.CharField(max_length=32,primary_key=True)
    title = models.CharField(max_length=300)
    content = models.CharField(max_length=65000)
    year = models.CharField(max_length=4)
    month = models.CharField(max_length=2)
    day = models.CharField(max_length=2)
    time = models.CharField(max_length=10).null
    reporter = models.CharField(max_length=100).null

    def __str__(self):
        return self.title
