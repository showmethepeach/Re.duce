from django.conf.urls import url, include
from api import views

urlpatterns = [
    url(r'^shop/$', views.shop_list),
    url(r'^shop/(?P<shop_id>\d+)/$', views.shop_detail),
    url(r'^shop/(?P<shop_id>\d+)/menus/$', views.menu_list),
    url(r'^shop/(?P<shop_id>\d+)/menus/(?P<menu_id>\d+)/$', views.menu_detail),
    url(r'^shop/(?P<shop_id>\d+)/reviews/$', views.review_list),
    url(r'^shop/(?P<shop_id>\d+)/reviews/(?P<review_id>\d+)/$', views.review_detail),

]
