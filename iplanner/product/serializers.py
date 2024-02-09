from rest_framework import serializers
from iplanner.project.serializers import ProjectFileSerializer
# from iplanner.survey.serializers import SurveyWithPagesSerializer, SurveySerializer
from .models import *



class ProductSerializer(serializers.ModelSerializer):
    image_details = ProjectFileSerializer(source='image', required=False, read_only=True)


    class Meta:
        model = Product
        fields = ('id', 'project', 'image', 'image_details', 'name' , 'description', 'product_type')

#
# class ProductFileSerializer(serializers.ModelSerializer):
#     project_file_details = ProjectFileSerializer(source='project_file', required=False, read_only=True)
#
#
#     class Meta:
#         model = ProductFile
#         fields = ('id', 'product', 'project_file', 'project_file_details')

#
# class ProductSurveySerializer(serializers.ModelSerializer):
#     survey_details = SurveySerializer(source='survey', required=False, read_only=True)
#
#     class Meta:
#         model = ProductSurvey
#         fields = ('id', 'product', 'survey', 'survey_details')
#
#
# class ProductSurveyWithdetailsSerializer(serializers.ModelSerializer):
#     survey_details = SurveyWithPagesSerializer(source='survey', required=False, read_only=True)
#
#     class Meta:
#         model = ProductSurvey
#         fields = ('id', 'product', 'survey', 'survey_details')


class ProductCompetitorSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductCompetitor
        fields = ('id', 'product', 'name', 'description', 'url', 'position')



