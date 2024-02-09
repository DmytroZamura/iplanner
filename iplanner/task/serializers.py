from rest_framework import serializers
from .models import Task
from iplanner.profile.serializers import UserWithProfileSerializer

class TaskSerializer(serializers.ModelSerializer):
    created_user_profile = UserWithProfileSerializer( source='created_user', required=False, read_only=True)
    assigned_user_profile = UserWithProfileSerializer( source='assigned_user', required=False, read_only=True)
    class Meta:
        model = Task
        fields = ('id','object_type', 'object_id', 'created_user','created_user_profile', 'assigned_user',
                  'assigned_user_profile',
                 'dead_line', 'name', 'description','comment', 'status', 'create_date' , 'update_date')





