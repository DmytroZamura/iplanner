
from rest_framework import serializers
from .models import *

from iplanner.profile.serializers import UserProfileSerializer, UserWithProfileSerializer





class ProjectSerializer(serializers.ModelSerializer):

    image_url = serializers.SerializerMethodField(read_only=True, required=False)

    # edit_mode = serializers.BooleanField(default=False, read_only=True, required=False)

    def get_image_url(self, obj):
        if obj.image:
            return self.context['request'].build_absolute_uri(obj.image_url)
    class Meta:
        model = Project
        fields = ('id', 'user', 'name','url','description', 'mission', 'vision', 'image','image_url', 'company_name', 'active')
        read_only_fields = ('image',)



class ProjectFileSerializer(serializers.ModelSerializer):
    # file_details = FileSerializer(source='file', required=False, read_only=True)
    file_url = serializers.SerializerMethodField()

    def get_file_url(self, obj):
        return self.context['request'].build_absolute_uri(obj.file_url)
    class Meta:
        model = ProjectFile
        fields = ('id', 'user', 'project', 'object_type', 'object_id', 'project_file', 'file_url','name', 'alt', 'type', 'create_date')
        read_only_fields = ('create_date', 'project_file')



class ProjectCompetitorSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectCompetitor
        fields = ('id', 'project', 'name','url','description', 'position')
        read_only_fields = ('position',)


class ProjectMockupSerializer(serializers.ModelSerializer):
    accepted_client_details = UserProfileSerializer(source='accepted_client', required=False, read_only=True)
    accepted_owner_details =  UserProfileSerializer(source='accepted_owner', required=False, read_only=True)
    class Meta:
        model = ProjectMockup
        fields = (
        'id', 'project', 'accepted_owner', 'accepted_owner_details','accepted_client', 'accepted_client_details',
        'version', 'create_date', 'update_date',
        'active', 'comment')
        read_only_fields = ('version',)



class ProjectMockupFilesSerializer(serializers.ModelSerializer):
    project_file_details = ProjectFileSerializer(source='project_file', required=False, read_only=True)
    class Meta:
        model = ProjectMockupFiles
        fields = (
        'id', 'project_mockup', 'project_file','project_file_details', 'create_date', 'update_date', 'comment')



class ProjectTeamSerializer(serializers.ModelSerializer):

    project_details = ProjectSerializer(source='project', required=False, read_only=True)
    class Meta:
        model = ProjectTeam
        fields = ('id', 'project', 'user','permission', 'user_profile')

class ProjectTeamdetailsSerializer(serializers.ModelSerializer):
    user_profile = UserWithProfileSerializer(source='user', required=False, read_only=True)
    project_details = ProjectSerializer(source='project', required=False, read_only=True)
    class Meta:
        model = ProjectTeam
        fields = ('id', 'project', 'user','permission', 'user_profile', 'project_details')

