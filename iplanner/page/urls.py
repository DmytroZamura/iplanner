from django.conf.urls import url

from iplanner.page import views


urlpatterns = [
    url(r'^page-types/(?P<language>.+)/$', views.page_types.as_view()),
    url(r'^page-type-user-survey-template/(?P<pk>.+)/$', views.page_type_user_survey_template_details.as_view()),
    url(r'^page-type-user-survey-templates/(?P<user>.+)/$', views.page_type_user_survey_templates.as_view()),
    url(r'^template-section/(?P<pk>.+)/$', views.template_section_details.as_view()),
    url(r'^template-sections/(?P<user>.+)/$', views.template_sections.as_view()),
    url(r'^template-section-move-down/(?P<pk>.+)/$', views.template_section_move_down.as_view()),
    url(r'^template-section-move-up/(?P<pk>.+)/$', views.template_section_move_up.as_view()),
    url(r'^default-template-sections(?P<user>.+)/$', views.default_template_sections.as_view()),
    url(r'^page-template/(?P<pk>.+)/$', views.page_template_details.as_view()),
    url(r'^page-templates/(?P<user>.+)/$', views.page_templates.as_view()),
    url(r'^default-page-templates(?P<user>.+)/$', views.default_page_templates.as_view()),
    url(r'^page/(?P<pk>.+)/$', views.page_details.as_view()),
    url(r'^pages/(?P<project>.+)/$', views.pages.as_view()),
    url(r'^page-move-down/(?P<pk>.+)/$', views.page_move_down.as_view()),
    url(r'^page-move-up/(?P<pk>.+)/$', views.page_move_up.as_view()),
    # url(r'^page-survey/(?P<pk>.+)/$', views.page_survey.as_view()),
    # url(r'^page-surveys/(?P<page>.+)/$', views.page_surveys.as_view()),
    url(r'^page-section/(?P<pk>.+)/$', views.page_section.as_view()),
    url(r'^page-sections/(?P<page>.+)/$', views.page_sections.as_view()),
    url(r'^page-section-move-down/(?P<pk>.+)/$', views.page_section_move_down.as_view()),
    url(r'^page-section-move-up/(?P<pk>.+)/$', views.page_section_move_up.as_view()),
    url(r'^page-mockup/(?P<pk>.+)/$', views.page_mockup_details.as_view()),
    url(r'^page-mockups/(?P<page>.+)/$', views.page_mockups.as_view()),
    url(r'^page-mockup-file/(?P<pk>.+)/$', views.page_mockup_file_details.as_view()),
    url(r'^page-mockups/(?P<mockup>.+)/$', views.page_mockup_files.as_view()),
    url(r'^page-competitor/(?P<pk>.+)/$', views.page_competitor_details.as_view()),
    url(r'^page-competitors/(?P<page>.+)/$', views.page_competitors.as_view()),
    url(r'^page-competitor-move-down/(?P<pk>.+)/$', views.page_competitor_move_down.as_view()),
    url(r'^page-competitor-move-up/(?P<pk>.+)/$', views.page_competitor_move_up.as_view()),
]
