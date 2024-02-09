
from rest_framework import serializers
from .models import *

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ('id','name', 'code')


class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = ('id','name', 'code')



class RecursiveSerializer(serializers.Serializer):
    def to_representation(self, value):
        serializer = self.parent.parent.__class__(value, context=self.context)
        return serializer.data

class SystemTagUrlSerializer(serializers.ModelSerializer):
    class Meta:
        model = SystemTagUrl
        fields = ('id', 'system_tag', 'url' , 'position', 'title' ,'description', 'image_url')
        read_only_fields = ('title' ,'description', 'image_url',)

class SystemTagSerializer(serializers.ModelSerializer):
    child_set = RecursiveSerializer(many=True, read_only=True)
    urls = SystemTagUrlSerializer (many=True, read_only=True)
    class Meta:
        model = SystemTag
        fields = ('id', 'language','name', 'tag','description','position', 'parent', 'child_set' , 'urls')



class SystemTagSearchSerializer(serializers.ModelSerializer):
    urls = SystemTagUrlSerializer(many=True, read_only=True)
    class Meta:
        model = SystemTag
        fields = ('id', 'language','name','tag', 'description','position','parent','urls')