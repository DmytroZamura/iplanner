from rest_framework import serializers
from .models import Comment
from iplanner.profile.serializers import UserWithProfileSerializer

class CommentSerializer(serializers.ModelSerializer):
    user_profile = UserWithProfileSerializer( source='user', required=False, read_only=True)
    class Meta:
        model = Comment
        fields = ('id','object_type', 'object_id','user', 'comment', 'user_profile', 'create_date' , 'update_date')



