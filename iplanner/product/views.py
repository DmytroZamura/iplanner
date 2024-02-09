from .serializers import *
from rest_framework import generics
from .models import *
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from rest_framework.response import Response

class products(generics.ListCreateAPIView):
    serializer_class = ProductSerializer
    def get_queryset(self):
        project = self.kwargs['project']
        return Product.objects.filter(project=project)

class product_details(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

#
# class product_files(generics.ListCreateAPIView):
#     serializer_class = ProductFileSerializer
#     def get_queryset(self):
#         product = self.kwargs['product']
#         return ProductFile.objects.filter(product=product)
#
# class product_file_details(generics.RetrieveUpdateDestroyAPIView):
#     serializer_class = ProductFileSerializer
#     queryset = ProductFile.objects.all()
#
#
# class product_surveys(generics.ListCreateAPIView):
#     serializer_class = ProductSurveySerializer
#     def get_queryset(self):
#         product = self.kwargs['product']
#         return ProductSurvey.objects.filter(product=product)
#
# class product_survey_details(generics.RetrieveUpdateDestroyAPIView):
#     serializer_class = ProductSurveyWithdetailsSerializer
#     queryset = ProductSurvey.objects.all()

class product_competitors(generics.ListCreateAPIView):
    serializer_class = ProductCompetitorSerializer

    def get_queryset(self):
        product = self.kwargs['product']
        return ProductCompetitor.objects.filter(product=product)

class product_competitor_details(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProductCompetitorSerializer
    queryset = ProductCompetitor.objects.all()


class product_competitor_move_down(APIView):


    def get_object(self, pk):
        return get_object_or_404(ProductCompetitor, id=pk)


    def put(self, request, pk):
        position = self.get_object(pk)

        position.move_down()
        serializer = ProductCompetitorSerializer(position)

        return Response(serializer.data)


class product_competitor_move_up(APIView):
    def get_object(self, pk):
        return get_object_or_404(ProductCompetitor, id=pk)

    def put(self, request, pk):
        position = self.get_object(pk)

        position.move_up()
        serializer = ProductCompetitorSerializer(position)

        return Response(serializer.data)
