from django.conf.urls import url, include
from api import views

urlpatterns = [
    url(r'^shops/$', views.shop_list),
    url(r'^shops/(?P<shop_id>\d+)/$', views.shop_detail),
    url(r'^shops/(?P<shop_id>\d+)/menus/$', views.menu_list),
    url(r'^shops/(?P<shop_id>\d+)/menus/(?P<menu_id>\d+)/$', views.menu_detail),
    url(r'^shops/(?P<shop_id>\d+)/reviews/$', views.review_list),
    url(r'^shops/(?P<shop_id>\d+)/reviews/(?P<review_id>\d+)/$', views.review_detail),
    url(r'^shops/(?P<shop_id>\d+)/orders/$', views.order_list),
    url(r'^shops/(?P<shop_id>\d+)/orders/(?P<order_id>\d+)/$', views.order_detail),

]
