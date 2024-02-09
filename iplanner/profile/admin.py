from __future__ import absolute_import
from django.contrib import admin
from .models import *



class UserProfileAdmin(admin.ModelAdmin):
    list_display = [field.name for field in UserProfile._meta.fields]

    class Meta:
        model = UserProfile

admin.site.register(UserProfile, UserProfileAdmin)


class UserProfileImageAdmin(admin.ModelAdmin):
    list_display = [field.name for field in UserProfileImage._meta.fields]

    class Meta:
        model = UserProfileImage

admin.site.register(UserProfileImage, UserProfileImageAdmin)

