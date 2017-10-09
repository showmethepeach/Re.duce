from django.conf.urls import url, include
from rest_framework_jwt.views import obtain_jwt_token
from user import views

urlpatterns = [
    url(r'^$', views.user_manager),
    url(r'^login/$', obtain_jwt_token),
]
