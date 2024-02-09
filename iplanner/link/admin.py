from __future__ import absolute_import
from django.contrib import admin
from .models import *

class LinkAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Link._meta.fields]

    class Meta:
        model = Link

admin.site.register(Link, LinkAdmin)