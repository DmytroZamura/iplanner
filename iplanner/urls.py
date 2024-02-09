"""iplanner URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.contrib import admin

from django.conf.urls import include, url

from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework import generics

from django.conf import settings
from django.conf.urls.static import static


# Serializers define the API representation.
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username')


# ViewSets define the view behavior.
class UserdetailsView(generics.RetrieveAPIView):
    lookup_field = 'username'
    serializer_class = UserSerializer
    queryset = User.objects.all()


# Routers provide an easy way of automatically determining the URL conf.
# router = routers.DefaultRouter()
# router.register(r'api/user/(?P<username>.+)/$', UserViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'api/', include('iplanner.general.urls')),
    url(r'api/', include('iplanner.profile.urls')),
    # url(r'api/', include('iplanner.file.urls')),
    url(r'api/', include('iplanner.project.urls')),
    url(r'api/', include('iplanner.survey.urls')),
    url(r'api/', include('iplanner.product.urls')),
    url(r'api/', include('iplanner.page.urls')),
    url(r'api/', include('iplanner.comments.urls')),
    url(r'api/', include('iplanner.task.urls')),
    url(r'api/', include('iplanner.link.urls')),
    url(r'^api/user/(?P<username>.+)/$', UserdetailsView.as_view()),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
