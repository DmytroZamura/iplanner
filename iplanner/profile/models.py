from __future__ import unicode_literals

# from django.db import models

from iplanner.general.models import *
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save

class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name='user_profile')
    interface_lang = models.ForeignKey(Language, blank=True, null=True)
    country = models.ForeignKey(Country, blank=True, null=True)
    email = models.CharField(max_length=100, null=True, blank=True)
    nickname = models.CharField(max_length=225, null=True, blank=True)
    first_name = models.CharField(max_length=225, null=True, blank=True )
    last_name = models.CharField(max_length=25, null=True, blank=True)
    job_title = models.CharField(max_length=150, blank=True, null=True)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "%s  %s" % (self.user.username, self.user_id)




def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance, interface_lang = 2)


def save_user_profile(sender, instance, **kwargs):
    instance.user_profile.save()

post_save.connect(create_user_profile, sender=User)
post_save.connect(save_user_profile, sender=User)


class UserProfileImage(models.Model):
    user = models.OneToOneField(User, related_name='user_image')
    image = models.ImageField(null=True, blank=True, upload_to='%Y/%m/%d/')

    def _get_image_url(self):
        if self.image:
            return self.image.url
        else:
            return None

    image_url = property(_get_image_url)

    def __str__(self):
        return self.user.username


def create_user_profile_image(sender, instance, created, **kwargs):
    if created:
        UserProfileImage.objects.create(user=instance)


def save_user_profile_image(sender, instance, **kwargs):
    instance.user_image.save()

post_save.connect(create_user_profile_image, sender=User)
post_save.connect(save_user_profile_image, sender=User)



