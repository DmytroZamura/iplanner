from rest_framework import serializers

# from iplanner.survey.serializers import SurveySerializer, SurveyWithPagesSerializer
from iplanner.general.serializers import SystemTagSerializer, LanguageSerializer
from iplanner.project.serializers import ProjectFileSerializer
from iplanner.profile.serializers import UserProfileSerializer
from iplanner.general.serializers import RecursiveSerializer
from .models import *



class PageTypeSerializer(serializers.ModelSerializer):
    system_tag_details = SystemTagSerializer(source='system_tag', required=False, read_only=True)
    language_details = LanguageSerializer(source='language', required=False, read_only=True)

    class Meta:
        model = PageType
        fields = ('id','system_tag', 'system_tag_details', 'name' , 'description',
                'language' ,'language_details')


class PageTypeUserTemplatesSerializer(serializers.ModelSerializer):
    page_type_details = PageTypeSerializer(source='page_type', required=False, read_only=True)


    class Meta:
        model = PageTypeUserTemplates
        fields = ('id', 'user', 'page_type', 'page_type_details', 'page_template')



class TemplateSectionSerializer(serializers.ModelSerializer):
    system_tag_details = SystemTagSerializer(source='system_tag', required=False, read_only=True)


    class Meta:
        model = PageTypeUserTemplates
        fields = ('id', 'user', 'system_tag', 'system_tag_details', 'name' , 'description', 'body', 'active')


class PageTemplateSerializer(serializers.ModelSerializer):
    system_tag_details = SystemTagSerializer(source='system_tag', required=False, read_only=True)


    class Meta:
        model = PageTemplate
        fields = ('id', 'user', 'system_tag', 'system_tag_details', 'name' , 'description', 'active')

class PageTemplateSectionSerializer(serializers.ModelSerializer):
    page_template_details = TemplateSectionSerializer(source='page_template', required=False, read_only=True)
    template_section_details = TemplateSectionSerializer(source='template_section', required=False, read_only=True)

    class Meta:
        model = PageTemplateSection
        fields = ('id', 'page_template', 'template_section', 'page_template_details', 'system_tag_details', 'position' )





class PageWithChildsSerializer(serializers.ModelSerializer):
    og_imgage_details = ProjectFileSerializer(source='og_imgage', required=False, read_only=True)
    accepted_owner_details = UserProfileSerializer(source='accepted_owner', required=False, read_only=True)
    accepted_client_details = UserProfileSerializer(source='accepted_client', required=False, read_only=True)
    child_set = RecursiveSerializer(many=True, read_only=True)

    class Meta:
        model = Page
        fields = ('id', 'parent', 'child_set', 'project', 'product', 'og_imgage', 'og_imgage_details', 'name',
                  'title', 'description', 'key_word', 'additional_key_word', 'page_body',
                  'active', 'comment', 'accepted_owner', 'accepted_owner_details', 'accepted_client', 'accepted_client_details', 'url',
                  'position')



class PageSerializer(serializers.ModelSerializer):
    og_imgage_details = ProjectFileSerializer(source='og_imgage', required=False, read_only=True)
    accepted_owner_details = UserProfileSerializer(source='accepted_owner', required=False, read_only=True)
    accepted_client_details = UserProfileSerializer(source='accepted_client', required=False, read_only=True)
    # child_set = RecursiveSerializer(many=True, read_only=True)

    class Meta:
        model = Page
        fields = ('id', 'parent', 'project', 'product', 'og_imgage', 'og_imgage_details', 'name',
                  'title', 'description', 'key_word', 'additional_key_word', 'page_body',
                  'active', 'comment', 'accepted_owner', 'accepted_owner_details', 'accepted_client', 'accepted_client_details', 'url',
                  'position')








class PageSectionSerializer(serializers.ModelSerializer):
    accepted_owner_details = UserProfileSerializer(source='accepted_owner', required=False, read_only=True)
    accepted_client_details = UserProfileSerializer(source='accepted_client', required=False, read_only=True)
    system_tag_details = SystemTagSerializer(source='system_tag', required=False, read_only=True)

    class Meta:
        model = Page
        fields = ('id', 'page', 'system_tag', 'system_tag_details','name', 'description', 'body', 'position', 'comment',
                  'accepted_owner', 'accepted_owner_details','accepted_client', 'accepted_client_details','active')

class PageMockupFilesSerializer(serializers.ModelSerializer):
    page_file_details = ProjectFileSerializer(source='page_file', required=False, read_only=True)

    class Meta:
        model = PageMockupFiles
        fields = ('id', 'page_mockup', 'comment', 'page_file', 'page_file_details')

class PageMockupSerializer(serializers.ModelSerializer):

    accepted_owner_details = UserProfileSerializer(source='accepted_owner', required=False, read_only=True)
    accepted_client_details = UserProfileSerializer(source='accepted_client', required=False, read_only=True)
    files =  PageMockupFilesSerializer(source='mockup_files', required=False, read_only=True)
    class Meta:
        model = PageMockup
        fields = ('id', 'page', 'comment', 'version',
                  'accepted_owner', 'accepted_owner_details','accepted_client', 'accepted_client_details','active', 'files')
        read_only_fields = ('version',)




class PageCompetitorSerializer(serializers.ModelSerializer):

    class Meta:
        model = PageMockupFiles
        fields = ('id', 'page', 'name', 'description', 'url' , 'position')
        read_only_fields = ('position',)


