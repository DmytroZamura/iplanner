

from .serializers import *
from rest_framework import generics
from .models import SystemTag




class countries_list(generics.ListCreateAPIView):
    queryset = Country.objects.all().order_by('name')
    serializer_class = CountrySerializer

class country_details(generics.RetrieveAPIView):
    queryset = Country.objects.all()
    serializer_class =  CountrySerializer

class country_search(generics.ListCreateAPIView):

    serializer_class = CountrySerializer

    def get_queryset(self):

        name = self.kwargs['name']
        return Country.objects.filter(name__icontains=name).order_by('name')

class languages_list(generics.ListCreateAPIView):
    queryset = Language.objects.all().order_by('name')
    serializer_class = LanguageSerializer


class language_search(generics.ListAPIView):

    serializer_class = LanguageSerializer

    def get_queryset(self):

        name = self.kwargs['name']
        return Language.objects.filter(name__icontains=name).order_by('name')

class language_details(generics.RetrieveUpdateDestroyAPIView):
    queryset = Language.objects.all()
    serializer_class =  LanguageSerializer


class system_tags_parent(generics.ListAPIView):
    serializer_class = SystemTagSerializer

    def get_queryset(self):
        pk = self.kwargs['pk']
        return SystemTag.objects.filter(id=pk)

class system_tags(generics.ListAPIView):
    # queryset = SystemTag.objects.filter(parent__isnull= True)
    serializer_class = SystemTagSerializer
    def get_queryset(self):
        language = self.kwargs['language']
        return SystemTag.objects.filter(parent__isnull= True, language=language)

class system_tag(generics.RetrieveAPIView):
    queryset = SystemTag.objects.all()
    serializer_class = SystemTagSerializer

class system_tag_urls(generics.ListAPIView):

    serializer_class =  SystemTagUrlSerializer

    def get_queryset(self):
        tag = self.kwargs['tag']
        return SystemTagUrl.objects.filter(system_tag=tag)

class system_tag_search(generics.ListAPIView):

    serializer_class = SystemTagSearchSerializer

    def get_queryset(self):

        tag = self.kwargs['tag']
        language = self.kwargs['language']
        return SystemTag.objects.filter(tag__icontains=tag, language=language).order_by('tag')