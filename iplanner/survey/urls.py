from django.conf.urls import url
from iplanner.survey import views


urlpatterns = [


    url(r'^survey/(?P<pk>.+)/$', views.survey_details.as_view()),
    url(r'^create-survey/', views.create_survey.as_view()),
    url(r'^survey-with-pages/(?P<pk>.+)/$', views.survey_with_pages.as_view()),
    url(r'^survey-image-upload/(?P<filename>.+)/(?P<pk>.+)/$', views.survey_image_upload.as_view()),
    url(r'^surveys-by-tag/(?P<project>.+)/(?P<tag>.+)/$', views.surveys_by_tag.as_view()),
    url(r'^template-surveys/(?P<user>.+)/(?P<object_type>.+)/$', views.template_surveys.as_view()),
    url(r'^user-template-surveys/(?P<user>.+)/$', views.user_template_surveys.as_view()),
    url(r'^user-surveys-sets/(?P<user>.+)/$', views.user_surveys_sets.as_view()),
    url(r'^surveys-sets/(?P<user>.+)/(?P<project_type>.+)/$', views.surveys_sets_list.as_view()),
    url(r'^surveys-set-details/(?P<pk>.+)/$', views.surveys_sets_details.as_view()),
    url(r'^surveys-in-set/(?P<set>.+)/(?P<object_type>.+)/$', views.surveys_in_set_list.as_view()),
    url(r'^delete-survey-in-set/(?P<pk>.+)/$', views.delete_survey_in_set.as_view()),
    url(r'^create-survey-in-set/(?P<pk>.+)/$', views.create_survey_in_set.as_view()),

    url(r'^survey-page/(?P<pk>.+)/$', views.survey_page_details.as_view()),
    url(r'^survey-page-with-fields/(?P<pk>.+)/$', views.survey_page_with_fields.as_view()),
    url(r'^survey-pages/(?P<survey>.+)/$', views.survey_pages.as_view()),
    url(r'^survey-page-move-down/(?P<pk>.+)/$', views.survey_page_move_down.as_view()),
    url(r'^survey-page-move-up/(?P<pk>.+)/$', views.survey_page_move_up.as_view()),
    url(r'^survey-page-field/(?P<pk>.+)/$', views.survey_page_field_details.as_view()),
    # url(r'^survey-page-field-with-answer/(?P<pk>.+)/$', views.survey_field_with_answer.as_view()),
    url(r'^survey-page-fields/(?P<page>.+)/$', views.survey_page_fields.as_view()),
    url(r'^survey-page-field-move-down/(?P<pk>.+)/$', views.survey_field_move_down.as_view()),
    url(r'^survey-page-field-move-up/(?P<pk>.+)/$', views.survey_field_move_up.as_view()),
    url(r'^survey-page-field-image-upload/(?P<filename>.+)/(?P<pk>.+)/$', views.survey_field_image_upload.as_view()),
    # url(r'^survey-field-answer/(?P<pk>.+)/$', views.survey_field_answer_details.as_view()),
    # url(r'^survey-field-answers/(?P<page>.+)/$', views.survey_field_answers.as_view()),



]
