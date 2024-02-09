#
# from rest_framework import serializers
# from .models import *
#
#
# class  FileSerializer(serializers.ModelSerializer):
#     file_url = serializers.SerializerMethodField()
#
#     def get_file_url(self, obj):
#         return self.context['request'].build_absolute_uri(obj.file_url)
#     class Meta:
#         model = File
#         fields = ('id', 'user_id', 'name', 'type', 'create_date', 'file_url')
#         read_only_fields = ('create_date',)
#
#
