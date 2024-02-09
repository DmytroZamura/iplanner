from django.conf.urls import url
from iplanner.comments import views


urlpatterns = [


    # url(r'^conversation/(?P<pk>[0-9]+)/$', views.conversation_details.as_view()),
    # url(r'^create-conversation/', views.create_conversation.as_view()),
    url(r'^comment/(?P<pk>[0-9]+)/$', views.comment_details.as_view()),
    url(r'^create-comment/', views.create_comment.as_view()),
    url(r'^comments/(?P<object_type>.+)/(?P<object_id>.+)/$', views.comments.as_view()),

]
