from django.conf.urls import url
from iplanner.link import views


urlpatterns = [
    url(r'^link/(?P<pk>[0-9]+)/$', views.link_details.as_view()),
    url(r'^create-link/', views.create_link.as_view()),
    url(r'^links/(?P<object_type>.+)/(?P<object_id>.+)/$', views.links.as_view()),

]