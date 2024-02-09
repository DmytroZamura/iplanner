
from rest_framework import serializers
from .models import *
# from iplanner.file.serializers import FileSerializer
from iplanner.general.serializers import LanguageSerializer
from iplanner.general.serializers import SystemTagSearchSerializer
from iplanner.page.serializers import PageTypeSerializer



class SurveySerializer(serializers.ModelSerializer):
    language_details = LanguageSerializer(source='language', required=False, read_only=True)
    system_tag_details = SystemTagSearchSerializer(source='system_tag', required=False, read_only=True)
    image_url = serializers.SerializerMethodField(read_only=True, required=False)
    page_type_details = PageTypeSerializer(source='page_type', required=False, read_only=True)
    object_type_name = serializers.SerializerMethodField()
    # edit_mode = serializers.BooleanField(default=False, read_only=True, required=False)

    def get_image_url(self, obj):

        if obj.image:
            return self.context['request'].build_absolute_uri(obj.image_url)

    def get_object_type_name(self, obj):
        return obj.get_object_type_display()

    class Meta:
        model = Survey
        fields = ('id', 'object_type', 'object_type_name', 'object_id', 'page_type', 'page_type_details', 'project',
                  'system_tag','system_tag_details','image','image_url', 'language','language_details',
                  'name','description', 'html_title',
                  'html_description', 'system','template' , 'is_publick', 'user', 'fields_qty' , 'completed_fields_qty', 'open_tasks_qty' )
        read_only_fields = ('system','image', 'fields_qty', 'completed_fields_qty', 'open_tasks_qty')


class SurveyPageSerializer(serializers.ModelSerializer):
    system_tag_details = SystemTagSearchSerializer(source='system_tag', required=False, read_only=True, many=False)
    class Meta:
        model = SurveyPage
        fields = ('id', 'survey', 'system_tag','system_tag_details', 'name', 'description' , 'position')


class SurveyFieldSerializer(serializers.ModelSerializer):
    system_tag_details = SystemTagSearchSerializer(source='system_tag', required=False, read_only=True)
    image_url = serializers.SerializerMethodField(read_only=True, required=False)

    def get_image_url(self, obj):
        if obj.image:
            return self.context['request'].build_absolute_uri(obj.image_url)

    class Meta:
        model = SurveyField
        fields = ('id', 'page', 'image_url', 'image', 'system_tag',
                  'system_tag_details', 'name', 'description', 'position', 'answer', 'completed', 'comments_qty',
                  'links_qty', 'tasks_qty', 'open_tasks_qty', 'project_files_qty')
        read_only_fields = ('image', 'comments_qty', 'links_qty', 'tasks_qty', 'open_tasks_qty', 'project_files_qty',)



# class SurveyAnswerSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = SurveyAnswer
#         fields = ('id', 'field', 'answer', 'update_user', 'create_user')

# class SurveyFieldWithAnswerSerializer(serializers.ModelSerializer):
#     system_tag_details = SystemTagSearchSerializer(source='system_tag', required=False, read_only=True)
#     image_url = serializers.SerializerMethodField()
#
#
#     def get_image_url(self, obj):
#         return self.context['request'].build_absolute_uri(obj.image_url)
#
#     class Meta:
#         model = SurveyField
#         fields = ('id', 'page', 'image','image_url', 'system_tag', 'system_tag_details', 'name', 'description', 'position', 'answer')
#         read_only_fields = ('image',)

class SurveyPageWithFieldsSerializer(serializers.ModelSerializer):
    system_tag_details = SystemTagSearchSerializer(source='system_tag', required=False, read_only=True, many=False)
    fields =  SurveyFieldSerializer (source='page_fields',many=True, read_only=True)
    class Meta:
        model = SurveyPage
        fields = ('id', 'survey', 'system_tag','system_tag_details', 'name', 'description' , 'position','fields')



class SurveyWithPagesSerializer(serializers.ModelSerializer):
    language_details = LanguageSerializer(source='language', required=False, read_only=True)
    system_tag_details = SystemTagSearchSerializer(source='system_tag', required=False, read_only=True)
    image_url = serializers.SerializerMethodField()
    pages = SurveyPageWithFieldsSerializer(many=True, read_only=True)

    def get_image_url(self, obj):
        if obj.image:
            return self.context['request'].build_absolute_uri(obj.image_url)


    class Meta:
        model = Survey
        fields = ('id', 'project', 'system_tag','system_tag_details','image','image_url', 'language',
                  'language_details', 'name','description', 'html_title',
                  'html_description' , 'template' , 'system', 'is_publick', 'user', 'pages')
        read_only_fields = ('system', 'image',)



class DefaultUserSurveySerializer(serializers.ModelSerializer):
    survey_details = SurveySerializer(source='survey', read_only=True)

    class Meta:
        model = DefaultUserSurvey
        fields = ('id', 'user', 'survey', 'survey_details')


class SurveysSetSerializer(serializers.ModelSerializer):
    language_details = LanguageSerializer(source='language', read_only=True)
    project_type_name = serializers.SerializerMethodField()
    def get_project_type_name(self, obj):
        return obj.get_project_type_display()
    class Meta:
        model = SurveysSet
        fields = ('id', 'user', 'project_type', 'project_type_name', 'language', 'language_details' ,'name', 'description', 'is_publick')


class SurveysInSetSerializer(serializers.ModelSerializer):
    survey_details = SurveySerializer(source='survey', read_only=True)
    # object_type_name = serializers.SerializerMethodField()

    def get_object_type_name(self, obj):
        return obj.get_object_type_display()

    class Meta:
        model = SurveysInSet
        fields = ('id', 'set', 'survey', 'survey_details')


# class TextSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     title = serializers.CharField()
#     description = serializers.CharField()
#     # text = serializers.CharField(style={'base_template': 'textarea.html'})
#     # key_words = serializers.