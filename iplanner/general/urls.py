from django.conf.urls import url
from iplanner.general import views


# from rest_framework import routers
#
# router = routers.DefaultRouter()
# router.register(r'heroes', heroes_list)

urlpatterns = [
    url(r'^countries/$', views.countries_list.as_view()),

    url(r'^country/(?P<pk>[0-9]+)/$', views.country_details.as_view()),

    url(r'^country-search/(?P<name>.+)/$', views.country_search.as_view()),
    url(r'^language-search/(?P<name>.+)/$', views.language_search.as_view()),
    url(r'^languages/$', views.languages_list.as_view()),

    url(r'^language/(?P<pk>[0-9]+)/$', views.language_details.as_view()),
    # url(r'^system-tags/(?P<pk>.+)/$', views.system_tags_parent.as_view()),
    url(r'^system-tag/(?P<pk>.+)/$', views.system_tag.as_view()),
    url(r'^system-tags/(?P<language>.+)/$', views.system_tags.as_view()),
    url(r'^system-tag-urls/(?P<tag>.+)/$', views.system_tag_urls.as_view()),
    url(r'^system-tag-search/(?P<language>.+)/(?P<tag>.+)/$', views.system_tag_search.as_view()),
]
