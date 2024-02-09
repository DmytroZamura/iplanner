from __future__ import unicode_literals

from django.db import models
import requests
from bs4 import BeautifulSoup


class Link(models.Model):
    OBJECT_TYPES = [
        (1, "1. answer"),
        (2, "2. page"),
        (3, "3. mockup")
    ]


    object_type = models.IntegerField(choices=OBJECT_TYPES, null=False, blank=False)
    object_id = models.IntegerField(null=False, blank=False)

    url = models.URLField( blank=False)

    image_url = models.CharField(max_length=350,blank=True, null=True)
    title = models.CharField(max_length=500,blank=True, null=True)
    description = models.CharField(max_length=500,blank=True, null=True)
    comment = models.TextField(max_length=2500, blank=True, null=True)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)


    class Meta:
        ordering = ["-create_date"]



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
        return super(Link, self).save(*args, **kwargs)

    def __str__(self):
        return self.url


def get_links_qty(object_type, object_id):
    qty = Link.objects.filter(object_type=object_type, object_id=object_id).count()
    if qty:
        return qty
    else:
        return 0
