
from .serializers import *
from rest_framework import generics
from .models import *
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

from rest_framework.views import APIView
from rest_framework.parsers import FileUploadParser






class user_profile_image_upload(APIView):
    parser_classes = (FileUploadParser,)

    def put(self, request, filename, user, format=None):

        file_obj = request.data['file']


        user_image = UserProfileImage.objects.get(user=user)
        user_image.image = file_obj


        try:
            user_image.save()
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        else:


            serializer = UserProfileImageSerializer(user_image, context={'request': request})

            return Response(serializer.data)



class user_profile_details(generics.RetrieveUpdateAPIView):
    serializer_class = UserProfileSerializer
    lookup_field = 'user'
    queryset = UserProfile.objects.all()


class user_profile_image(generics.RetrieveAPIView):
    serializer_class = UserProfileImageSerializer
    lookup_field = 'user'
    queryset = UserProfileImage.objects.all()


class user_profile_check(APIView):
    def get_object(self, pk):
        return get_object_or_404(UserProfile, user=pk)


    def put(self, request, pk):

        profile = self.get_object(pk)

        if not profile.nickname:
            serializer = UserProfileSerializer(profile, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response()
