from django.conf.urls import url
from iplanner.profile import views
# from .views import *

# from rest_framework import routers
#
# router = routers.DefaultRouter()
# router.register(r'heroes', heroes_list)

urlpatterns = [
    # url(r'^profiles$', views.user_profiles_list.as_view()),
    url(r'^profile/(?P<user>.+)/$', views.user_profile_details.as_view()),
    url(r'^profile-image/(?P<user>.+)/$', views.user_profile_image.as_view()),

    url(r'^profile-check/(?P<pk>.+)/$', views.user_profile_check.as_view()),
    # url(r'^profile-update/(?P<pk>.+)/$', views.user_profile_path.as_view()),
    # url(r'^profile-image-upload/(?P<user>.+)/$', views.user_profile_image_upload.as_view()),
    url(r'^profile-image-upload/(?P<filename>.+)/(?P<user>.+)/$', views.user_profile_image_upload.as_view())


]
