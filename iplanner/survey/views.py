from .serializers import *
from rest_framework import generics
from .models import *
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.parsers import FileUploadParser
from rest_framework import status
from django.db.models import Q
from iplanner.profile.models import UserProfile



class create_survey(generics.CreateAPIView):
    serializer_class = SurveySerializer
    queryset = Survey.objects.all()

class survey_details(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = SurveySerializer
    queryset = Survey.objects.all()

class surveys_by_tag(generics.ListCreateAPIView):
    serializer_class = SurveySerializer
    def get_queryset(self):
        project = self.kwargs['project']
        tag = self.kwargs['tag']
        return Survey.objects.filter(project=project, system_tag__tag=tag)



class user_surveys_sets(generics.ListCreateAPIView):
    serializer_class = SurveysSetSerializer
    def get_queryset(self):
        user = self.kwargs['user']

        return SurveysSet.objects.filter(user=user)


class surveys_sets_list(generics.ListAPIView):
    serializer_class = SurveysSetSerializer

    def get_queryset(self):

        user = self.kwargs['user']
        project_type = self.kwargs['project_type']

        language = UserProfile.objects.get(user=user).interface_lang

        return SurveysSet.objects.filter(Q(system = True) | Q(user=user), Q(language=language), Q(project_type=project_type))

class surveys_sets_details(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = SurveysSetSerializer
    queryset = SurveysSet.objects.all()


class surveys_in_set_list(generics.ListAPIView):
    serializer_class = SurveysInSetSerializer

    def get_queryset(self):
        set = self.kwargs['set']
        object_type = self.kwargs['object_type']

        return SurveysInSet.objects.filter(set=set, survey__object_type=object_type)

class delete_survey_in_set(generics.DestroyAPIView):
    serializer_class = SurveysInSetSerializer
    queryset = SurveysInSet.objects.all()

class create_survey_in_set(generics.CreateAPIView):
    serializer_class = SurveysInSetSerializer
    queryset = SurveysInSet.objects.all()



class template_surveys(generics.ListAPIView):
    serializer_class = SurveySerializer

    def get_queryset(self):

        user = self.kwargs['user']
        # functionality_type = self.kwargs['functionality_type']
        language = UserProfile.objects.get(user=user).interface_lang
        object_type = self.kwargs['object_type']

        return Survey.objects.filter(Q(template=True,  object_type=object_type, system_tag__language=language),
                                     Q(system = True, is_publick=True) | Q(user=user))


class user_template_surveys(generics.ListCreateAPIView):
    serializer_class = SurveySerializer
    def get_queryset(self):

        user = self.kwargs['user']
        # functionality_type = self.kwargs['functionality_type']
        # language = UserProfile.objects.get(user=user).interface_lang

        return Survey.objects.filter(user=user, project=None)

class survey_pages(generics.ListCreateAPIView):
    serializer_class = SurveyPageWithFieldsSerializer
    def get_queryset(self):
        survey = self.kwargs['survey']
        return SurveyPage.objects.filter(survey=survey)

class survey_page_details(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = SurveyPageSerializer
    queryset = SurveyPage.objects.all()

class survey_page_fields(generics.ListCreateAPIView):
    serializer_class = SurveyFieldSerializer
    def get_queryset(self):

        page = self.kwargs['page']
        return SurveyField.objects.filter(page=page)


class survey_page_field_details(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = SurveyFieldSerializer
    queryset = SurveyField.objects.all()

# class survey_field_answers(generics.ListCreateAPIView):
#     serializer_class = SurveyAnswerSerializer
#     def get_queryset(self):
#         field = self.kwargs['field']
#         return SurveyAnswer.objects.filter(field=field)


# class survey_field_answer_details(generics.RetrieveUpdateDestroyAPIView):
#     serializer_class = SurveyAnswerSerializer
#     queryset = SurveyAnswer.objects.all()

# class survey_field_with_answer(generics.RetrieveUpdateDestroyAPIView):
#     serializer_class = SurveyFieldWithAnswerSerializer
#     queryset = SurveyField.objects.all()

class survey_page_with_fields(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = SurveyPageWithFieldsSerializer
    queryset = SurveyPage.objects.all()


class survey_with_pages(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = SurveyWithPagesSerializer
    queryset = Survey.objects.all()

class survey_page_move_down(APIView):
    def get_object(self, pk):
        return get_object_or_404(SurveyPage, id=pk)


    def put(self, request, pk):
        position = self.get_object(pk)

        position.move_down()
        serializer = SurveyPageSerializer(position, context={'request': request})

        return Response(serializer.data)


class survey_page_move_up(APIView):
    def get_object(self, pk):
        return get_object_or_404(SurveyPage, id=pk)

    def put(self, request, pk):
        position = self.get_object(pk)

        position.move_up()
        serializer = SurveyPageSerializer(position, context={'request': request})

        return Response(serializer.data)



class survey_field_move_down(APIView):


    def get_object(self, pk):
        return get_object_or_404(SurveyField, id=pk)


    def put(self, request, pk):

        position = self.get_object(pk)

        position.move_down()
        serializer = SurveyFieldSerializer(position, context={'request': request})

        return Response(serializer.data)


class survey_field_move_up(APIView):
    def get_object(self, pk):
        return get_object_or_404(SurveyField, id=pk)

    def put(self, request, pk):
        position = self.get_object(pk)

        position.move_up()
        serializer = SurveyFieldSerializer(position, context={'request': request})

        return Response(serializer.data)


class survey_image_upload(APIView):
    parser_classes = (FileUploadParser,)

    def put(self, request, filename, pk, format=None):

        file_obj = request.data['file']


        survey_image = Survey.objects.get(pk=pk)
        survey_image.image = file_obj


        try:
            survey_image.save()
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        else:


            serializer = SurveySerializer(survey_image, context={'request': request})

            return Response(serializer.data)



class survey_field_image_upload(APIView):
    parser_classes = (FileUploadParser,)

    def put(self, request, filename, pk, format=None):

        file_obj = request.data['file']

        survey_field_image = SurveyField.objects.get(pk=pk)
        survey_field_image.image = file_obj


        try:
            survey_field_image.save()
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        else:


            serializer = SurveyFieldSerializer(survey_field_image, context={'request': request})

            return Response(serializer.data)


