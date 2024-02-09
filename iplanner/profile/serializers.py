
from rest_framework import serializers
from .models import *
from iplanner.general.serializers import *





class UserProfileSerializer(serializers.ModelSerializer):
    language_details = LanguageSerializer(source='interface_lang', required=False, read_only=True)
    country_details = CountrySerializer(source='country', required=False, read_only=True)
    class Meta:
        model = UserProfile
        fields = ('id', 'user_id', 'email','nickname','first_name', 'last_name', 'job_title',
                  'interface_lang', 'interface_lang','country','language_details', 'country_details')
        # read_only_fields = ('avatar',)



class UserProfileImageSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()

    def get_image_url(self, obj):
        return self.context['request'].build_absolute_uri(obj.image_url)

    class Meta:
        model = UserProfileImage
        fields = ('id', 'user_id', 'image', 'image_url')


class UserProfileShortSerializer(serializers.ModelSerializer):



    class Meta:
        model = UserProfile
        fields = ('id', 'user_id', 'nickname','first_name','last_name')


class UserWithProfileSerializer(serializers.ModelSerializer):
    user_image = UserProfileImageSerializer(many=False, read_only=True)
    user_profile = UserProfileShortSerializer(required=False, read_only=True)
    class Meta:
        model = User
        fields = ('id', 'user_profile', 'user_image')