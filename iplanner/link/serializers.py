
from rest_framework import serializers
from .models import *

class LinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Link
        fields = ('id', 'url', 'object_id', 'object_type', 'comment', 'title' ,'description', 'image_url')
        read_only_fields = ('title' ,'description', 'image_url',)
