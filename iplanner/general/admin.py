from __future__ import absolute_import
from django.contrib import admin
from .models import *


class CountryAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Country._meta.fields]

    class Meta:
        model = Country

admin.site.register(Country, CountryAdmin)

class LanguageAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Language._meta.fields]

    class Meta:
        model = Language

admin.site.register(Language, LanguageAdmin)

class SystemTagAdmin(admin.ModelAdmin):
    list_display = [field.name for field in SystemTag._meta.fields]

    class Meta:
        model = SystemTag

admin.site.register(SystemTag, SystemTagAdmin)


class SystemTagUrlAdmin(admin.ModelAdmin):
    list_display = [field.name for field in SystemTagUrl._meta.fields]

    class Meta:
        model = SystemTagUrl

admin.site.register(SystemTagUrl, SystemTagUrlAdmin)