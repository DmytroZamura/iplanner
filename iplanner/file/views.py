#
# from .serializers import *
# from rest_framework import generics
# from .models import *
# from rest_framework.response import Response
# from rest_framework import status
#
# from rest_framework.views import APIView
# from rest_framework.parsers import FileUploadParser
#
#
#
# class file_upload(APIView):
#     parser_classes = (FileUploadParser,)
#
#     def post(self, request, filename, user, type, format=None):
#
#         file_obj = request.data['file']
#         try:
#             user_file = File.objects.create(file=file_obj, user=user, name=filename, type=type)
#         except:
#             return Response(status=status.HTTP_400_BAD_REQUEST)
#         else:
#             serializer = FileSerializer(user_file, context={'request': request})
#             return Response(serializer)
#
# class file_details(generics.RetrieveUpdateDestroyAPIView):
#     serializer_class = FileSerializer
#     queryset = File.objects.all()
#
#
# class files(generics.ListAPIView):
#     serializer_class = FileSerializer
#
#
#     def get_queryset(self):
#         user = self.kwargs['user']
#         return File.objects.filter(user=user)
#
#
