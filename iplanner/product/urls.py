from django.conf.urls import url, include

from iplanner.product import views


urlpatterns = [

    url(r'^product/(?P<pk>.+)/$', views.product_details.as_view()),
    url(r'^products/(?P<project>.+)/$', views.products.as_view()),
    # url(r'^product-file/(?P<pk>.+)/$', views.product_file_details.as_view()),
    # url(r'^product-files/(?P<product>.+)/$', views.product_files.as_view()),
    # url(r'^product-survey/(?P<pk>.+)/$', views.product_survey_details.as_view()),
    # url(r'^product-surveys/(?P<product>.+)/$', views.product_surveys.as_view()),
    url(r'^product-competitor/(?P<pk>.+)/$', views.product_competitor_details.as_view()),
    url(r'^product-competitors/(?P<product>.+)/$', views.product_competitors.as_view()),
    url(r'^product-competitor-move-down/(?P<pk>.+)/$', views.product_competitor_move_down.as_view()),
    url(r'^product-competitor-move-up/(?P<pk>.+)/$', views.product_competitor_move_up.as_view()),


]
