from __future__ import absolute_import
from django.contrib import admin
from .models import *


# class ConversationAdmin(admin.ModelAdmin):
#     list_display = [field.name for field in Conversation._meta.fields]
#
#     class Meta:
#         model = Conversation
#
# admin.site.register(Conversation, ConversationAdmin)

class CommentAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Comment._meta.fields]

    class Meta:
        model = Comment

admin.site.register(Comment, CommentAdmin)