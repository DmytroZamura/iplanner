from __future__ import unicode_literals

from django.db import models
from django.db.models import Max
import requests
from bs4 import BeautifulSoup


class Country(models.Model):
    code = models.CharField(max_length=3, null=True, unique=True)
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class Language(models.Model):
    code = models.CharField(max_length=3, unique=True)
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class SystemTag(models.Model):
    FUNCTIONALITY_TYPES = [
        (1, "1. Project general"),
        (2, "2. Product"),
        (3, "3. Page")
    ]

    parent = models.ForeignKey('self', related_name='child_set', null=True, blank=True, default=None)
    language = models.ForeignKey(Language, blank=False, default=1)
    name = models.CharField(max_length=40, blank=False)
    description = models.TextField(blank=True)
    position = models.PositiveIntegerField(null=True, blank=True)
    tag = models.CharField(max_length=40, blank=False)
    functionality_type = models.IntegerField(choices=FUNCTIONALITY_TYPES, null=True,blank=True)



    class Meta:
        ordering = ["position"]

    def save(self, *args, **kwargs):
        if self.position is None:
            max_position = self.parent.child_set.aggregate(Max("position"))
            self.position = (max_position.get("position__max") or 0) + 1
        return super(SystemTag, self).save(*args, **kwargs)

    def __str__(self):
        return "%s  %s" % (self.name, self.id)

class SystemTagUrl(models.Model):
    system_tag = models.ForeignKey(SystemTag, related_name='urls')

    url = models.URLField( blank=False)
    position = models.PositiveIntegerField(null=True, blank=True)
    image_url = models.CharField(max_length=350,blank=True, null=True)
    title = models.CharField(max_length=500,blank=True, null=True)
    description = models.CharField(max_length=500,blank=True, null=True)



    class Meta:
        ordering = ["position"]

    def save(self, *args, **kwargs):
        if self.url:
            headers = {
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:45.0) Gecko/20100101 Firefox/45.0'
            }

            page = requests.get(self.url, headers=headers)

            soup = BeautifulSoup(page.text, 'html.parser')
            title = soup.title.string
            if title:
                self.title = title
            else:
                self.title = None

            desc = soup.find(attrs={"name": "description"})
            if desc:
                self.description = desc['content'].strip()
            else:
                self.description = None
            og_image = soup.find(attrs={"property": "og:image"})

            if og_image:
                self.image_url = og_image['content'].strip()
            else:
                self.image_url = None
        return super(SystemTagUrl, self).save(*args, **kwargs)

    def __str__(self):
        return self.url