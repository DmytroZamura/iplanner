from __future__ import absolute_import
from django.contrib import admin
from .models import *


class ProductAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Product._meta.fields]

    class Meta:
        model = Product

admin.site.register(Product, ProductAdmin)

#
# class ProductFileAdmin(admin.ModelAdmin):
#     list_display = [field.name for field in ProductFile._meta.fields]
#
#     class Meta:
#         model = ProductFile
#
# admin.site.register(ProductFile, ProductFileAdmin)
#
#
# class ProductSurveyAdmin(admin.ModelAdmin):
#     list_display = [field.name for field in ProductSurvey._meta.fields]
#
#     class Meta:
#         model = ProductSurvey
#
# admin.site.register(ProductSurvey, ProductSurveyAdmin)


class ProductCompetitorAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ProductCompetitor._meta.fields]

    class Meta:
        model = ProductCompetitor

admin.site.register(ProductCompetitor, ProductCompetitorAdmin)
