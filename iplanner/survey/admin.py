from __future__ import absolute_import
from django.contrib import admin
from .models import *



class SurveyAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Survey._meta.fields]

    class Meta:
        model = Survey

admin.site.register(Survey, SurveyAdmin)


class SurveyPageAdmin(admin.ModelAdmin):
    list_display = [field.name for field in SurveyPage._meta.fields]

    class Meta:
        model = Survey

admin.site.register(SurveyPage, SurveyPageAdmin)


class SurveyFieldAdmin(admin.ModelAdmin):
    list_display = [field.name for field in SurveyField._meta.fields]

    class Meta:
        model = Survey

admin.site.register(SurveyField, SurveyFieldAdmin)

# class SurveyAnswerAdmin(admin.ModelAdmin):
#     list_display = [field.name for field in SurveyAnswer._meta.fields]
#
#     class Meta:
#         model = SurveyAnswer
#
# admin.site.register(SurveyAnswer, SurveyAnswerAdmin)

class DefaultSurveyAdmin(admin.ModelAdmin):
    list_display = [field.name for field in DefaultSurvey._meta.fields]

    class Meta:
        model = DefaultSurvey

admin.site.register(DefaultSurvey, DefaultSurveyAdmin)


class DefaultUserSurveyAdmin(admin.ModelAdmin):
    list_display = [field.name for field in DefaultUserSurvey._meta.fields]

    class Meta:
        model = DefaultUserSurvey

admin.site.register(DefaultUserSurvey, DefaultUserSurveyAdmin)


class SurveysSetAdmin(admin.ModelAdmin):
    list_display = [field.name for field in SurveysSet._meta.fields]

    class Meta:
        model = SurveysSet

admin.site.register(SurveysSet, SurveysSetAdmin)

class SurveysInSetAdmin(admin.ModelAdmin):
    list_display = [field.name for field in SurveysInSet._meta.fields]

    class Meta:
        model = SurveysInSet

admin.site.register(SurveysInSet, SurveysInSetAdmin)