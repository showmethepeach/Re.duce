from django.conf.urls import url, include
from rest_framework import routers
from owner import views

urlpatterns = [
    url(r'^my-shop/$', views.my_shop_list),
    url(r'^my-shop/(?P<shop_id>\d+)/$', views.my_shop_detail),
    url(r'^my-shop/(?P<shop_id>\d+)/menus/$', views.menu_list),
    url(r'^my-shop/(?P<shop_id>\d+)/menus/(?P<menu_id>\d+)/$', views.menu_detail),
    url(r'^my-shop/(?P<shop_id>\d+)/reviews/$', views.review_list),
    url(r'^my-shop/(?P<shop_id>\d+)/reviews/(?P<review_id>\d+)/$', views.review_detail),
]
