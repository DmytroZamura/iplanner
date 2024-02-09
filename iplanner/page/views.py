from .serializers import *
from rest_framework import generics
from .models import *
from django.db.models import Q
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView



class page_types(generics.ListAPIView):
    serializer_class = PageTypeUserTemplatesSerializer
    def get_queryset(self):
        language = self.kwargs['language']
        return PageType.objects.filter(language=language)

class page_type_user_survey_templates(generics.ListCreateAPIView):
    serializer_class = PageTypeUserTemplatesSerializer
    def get_queryset(self):
        user = self.kwargs['user']
        return PageTypeUserTemplates.objects.filter(user=user)

class page_type_user_survey_template_details(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PageTypeUserTemplatesSerializer
    queryset = PageTypeUserTemplates.objects.all()


class template_sections(generics.ListCreateAPIView):
    serializer_class = TemplateSectionSerializer
    def get_queryset(self):
        user = self.kwargs['user']
        return TemplateSection.objects.filter(user=user, active=True)

class default_template_sections(generics.ListAPIView):
    serializer_class = TemplateSectionSerializer
    def get_queryset(self):
        user = self.kwargs['user']
        return TemplateSection.objects.filter(Q(system = True, active=True) | Q(user=user, active=True))

class template_section_details(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TemplateSectionSerializer
    queryset = TemplateSection.objects.all()


class template_section_move_down(APIView):
    def get_object(self, pk):
        return get_object_or_404(TemplateSection, id=pk)


    def put(self, request, pk):
        position = self.get_object(pk)

        position.move_down()
        serializer = TemplateSectionSerializer(position)

        return Response(serializer.data)


class template_section_move_up(APIView):
    def get_object(self, pk):
        return get_object_or_404(TemplateSection, id=pk)

    def put(self, request, pk):
        position = self.get_object(pk)

        position.move_up()
        serializer = TemplateSectionSerializer(position)

        return Response(serializer.data)

class page_templates(generics.ListCreateAPIView):
    serializer_class = PageTemplateSerializer
    def get_queryset(self):
        user = self.kwargs['user']
        return PageTemplate.objects.filter(user=user, active=True)

class default_page_templates(generics.ListAPIView):
    serializer_class = PageTemplateSerializer
    def get_queryset(self):
        user = self.kwargs['user']
        return PageTemplate.objects.filter(Q(system = True, active=True) | Q(user=user, active=True))

class page_template_details(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PageTemplateSerializer
    queryset = PageTemplate.objects.all()

class pages(generics.ListCreateAPIView):
        serializer_class = PageWithChildsSerializer
        def get_queryset(self):
            project = self.kwargs['project']
            return Page.objects.filter(project=project, active=True, parent=None)


class page_details(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PageSerializer
    queryset = Page.objects.all()



class page_move_down(APIView):
    def get_object(self, pk):
        return get_object_or_404(Page, id=pk)


    def put(self, request, pk):
        position = self.get_object(pk)

        position.move_down()
        serializer = PageSerializer(position)

        return Response(serializer.data)


class page_move_up(APIView):
    def get_object(self, pk):
        return get_object_or_404(Page, id=pk)

    def put(self, request, pk):
        position = self.get_object(pk)

        position.move_up()
        serializer = PageSerializer(position)

        return Response(serializer.data)


# class page_surveys(generics.ListCreateAPIView):
#     serializer_class = PageSurveySerializer
#
#     def get_queryset(self):
#         page = self.kwargs['page']
#         return PageSurvey.objects.filter(page=page)
#
#
# class page_survey(generics.RetrieveUpdateDestroyAPIView):
#     serializer_class = PageSectionSerializer
#     queryset = PageSurvey.objects.all()


class page_sections(generics.ListCreateAPIView):
    serializer_class = PageSectionSerializer

    def get_queryset(self):
        page = self.kwargs['page']
        return PageSection.objects.filter(page=page)


class page_section(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PageSectionSerializer
    queryset = PageSection.objects.all()




class page_section_move_down(APIView):
    def get_object(self, pk):
        return get_object_or_404(Page, id=pk)


    def put(self, request, pk):
        position = self.get_object(pk)

        position.move_down()
        serializer = PageSectionSerializer(position)

        return Response(serializer.data)


class page_section_move_up(APIView):
    def get_object(self, pk):
        return get_object_or_404(Page, id=pk)

    def put(self, request, pk):
        position = self.get_object(pk)

        position.move_up()
        serializer = PageSectionSerializer(position)

        return Response(serializer.data)


class page_competitor_details(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PageCompetitorSerializer
    queryset = PageCompetitor.objects.all()


class page_competitors(generics.ListCreateAPIView):
    serializer_class = PageCompetitorSerializer

    def get_queryset(self):
        page = self.kwargs['page']
        return PageCompetitor.objects.filter(page=page)


class page_competitor_move_down(APIView):


    def get_object(self, pk):
        return get_object_or_404(PageCompetitor, id=pk)


    def put(self, request, pk):
        position = self.get_object(pk)

        position.move_down()
        serializer = PageCompetitorSerializer(position)

        return Response(serializer.data)


class page_competitor_move_up(APIView):
    def get_object(self, pk):
        return get_object_or_404(PageCompetitor, id=pk)

    def put(self, request, pk):
        position = self.get_object(pk)

        position.move_up()
        serializer = PageCompetitorSerializer(position)

        return Response(serializer.data)


class page_mockup_details(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PageMockupSerializer
    queryset = PageMockup.objects.all()


class page_mockups(generics.ListCreateAPIView):
    serializer_class = PageMockupSerializer

    def get_queryset(self):
        page = self.kwargs['page']
        return PageMockup.objects.filter(page=page)


class page_mockup_file_details(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PageMockupFilesSerializer
    queryset = PageMockupFiles.objects.all()


class page_mockup_files(generics.ListCreateAPIView):
    serializer_class = PageMockupFilesSerializer

    def get_queryset(self):
        mockup = self.kwargs['mockup']
        return PageMockupFiles.objects.filter(page_mockup=mockup)