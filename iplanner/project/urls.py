from django.conf.urls import url
from iplanner.project import views


urlpatterns = [

    url(r'^projects/(?P<user>.+)/$', views.projects.as_view()),
    url(r'^user-projects-list/(?P<user>.+)/$', views.user_projects_list.as_view()),
    url(r'^project/(?P<pk>.+)/$', views.project_details.as_view()),
    url(r'^project-image-upload/(?P<filename>.+)/(?P<pk>.+)/$', views.project_image_upload.as_view()),
    url(r'^project-file-upload/(?P<filename>.+)/(?P<project>[0-9]+)/(?P<object_type>[0-9]+)/(?P<object_id>[0-9]+)/(?P<user>[0-9]+)/(?P<type>.+)/$', views.project_file_upload.as_view()),
    url(r'^project-file/(?P<pk>.+)/$', views.project_file_details.as_view()),
    url(r'^project-files/(?P<project>.+)/$', views.project_files.as_view()),
    url(r'^project-files-by-type/(?P<project>.+)/(?P<type>.+)/$', views.project_files_by_type.as_view()),
    url(r'^project-files-by-object/(?P<project>.+)/(?P<object_type>.+)/(?P<object_id>.+)/$', views.project_files_by_object.as_view()),
    # url(r'^project-files-by-object/(?P<object_type>.+)/(?P<object_id>.+)/$', views.project_files_by_object.as_view()),

    url(r'^project-files-query/(?P<project>.+)/(?P<query>.+)/$', views.project_files_guery.as_view()),
    url(r'^project-competitor/(?P<pk>.+)/$', views.project_competitor_details.as_view()),
    url(r'^project-competitors/(?P<project>.+)/$', views.project_competitors.as_view()),
    url(r'^project-competitor-move-down/(?P<pk>.+)/$', views.project_competitor_move_down.as_view()),
    url(r'^project-competitor-move-up/(?P<pk>.+)/$', views.project_competitor_move_up.as_view()),
    url(r'^website-keywords-analysis/(?P<competitor>.+)/$', views.website_keywords_analysis.as_view()),
    url(r'^project-mockup/(?P<pk>.+)/$', views.project_mockup_details.as_view()),
    url(r'^project-mockups/(?P<project>.+)/$', views.project_mockups.as_view()),
    url(r'^project-mockup-file/(?P<pk>.+)/$', views.project_mockup_file_details.as_view()),
    url(r'^project-mockups/(?P<mockup>.+)/$', views.project_mockup_files.as_view()),
    url(r'^project-team-list/(?P<project>.+)/$', views.project_team_list.as_view()),
    url(r'^project-team-member/(?P<pk>.+)/$', views.project_team_member.as_view()),
]
