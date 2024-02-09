from __future__ import absolute_import
from django.contrib import admin
from .models import *



class PageTypeAdmin(admin.ModelAdmin):
    list_display = [field.name for field in PageType._meta.fields]

    class Meta:
        model = PageType

admin.site.register(PageType, PageTypeAdmin)



class PageTypeUserSurveyTemplatesAdmin(admin.ModelAdmin):
    list_display = [field.name for field in PageTypeUserTemplates._meta.fields]

    class Meta:
        model = PageTypeUserTemplates

admin.site.register(PageTypeUserTemplates, PageTypeUserSurveyTemplatesAdmin)


class PageAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Page._meta.fields]

    class Meta:
        model = Page

admin.site.register(Page, PageAdmin)


# class PageSurveyAdmin(admin.ModelAdmin):
#     list_display = [field.name for field in PageSurvey._meta.fields]
#
#     class Meta:
#         model = PageSurvey
#
# admin.site.register(PageSurvey, PageSurveyAdmin)

class TemplateSectionAdmin(admin.ModelAdmin):
    list_display = [field.name for field in TemplateSection._meta.fields]

    class Meta:
        model = TemplateSection

admin.site.register(TemplateSection, TemplateSectionAdmin)

class PageTemplateAdmin(admin.ModelAdmin):
    list_display = [field.name for field in PageTemplate._meta.fields]

    class Meta:
        model = PageTemplate

admin.site.register(PageTemplate, PageTemplateAdmin)

class PageTemplateSectionAdmin(admin.ModelAdmin):
    list_display = [field.name for field in PageTemplateSection._meta.fields]

    class Meta:
        model = PageTemplateSection

admin.site.register(PageTemplateSection, PageTemplateSectionAdmin)