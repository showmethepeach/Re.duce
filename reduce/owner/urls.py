from django.conf.urls import url, include
from owner import views

urlpatterns = [
    url(r'^my-shop/$', views.shop_list),
    url(r'^my-shop/(?P<name>[a-z]+)/$', views.shop_detail),
]
