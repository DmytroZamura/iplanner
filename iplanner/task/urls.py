from django.conf.urls import url
from iplanner.task import views


urlpatterns = [


    url(r'^task/(?P<pk>[0-9]+)/$', views.task_details.as_view()),
    url(r'^create-task/', views.create_task.as_view()),
    url(r'^tasks/(?P<object_type>.+)/(?P<object_id>.+)/$', views.tasks.as_view()),

]
