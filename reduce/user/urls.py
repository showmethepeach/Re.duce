from django.conf.urls import url, include
from rest_framework import routers
from rest_framework_jwt.views import obtain_jwt_token
from user import views

urlpatterns = [
    url(r'^$', views.user_detail),
    url(r'^signup/$', views.user_signup),
    url(r'^login/$', obtain_jwt_token),
]
