from django.shortcuts import get_object_or_404
from rest_framework import generics, filters
from rest_framework.permissions import IsAuthenticated
from owner.models import Shop, Menu
from owner.serializers import MyShopSerializer, MenuSerializer,MyShopCreateUpdateSerializer, MenuCreateUpdateSerializer
from owner.permissions import IsOwner

from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAdminUser,
    IsAuthenticatedOrReadOnly,

    )

#제네릭 뷰를 이용하여 코드 길이를 줄임
from rest_framework.generics import (
    CreateAPIView,
    DestroyAPIView,
    ListAPIView,
    UpdateAPIView,
    RetrieveAPIView,
    RetrieveUpdateAPIView
    )

class MyShopList(generics.ListCreateAPIView):
    # 사장별 가게 리스트
    serializer_class = MyShopSerializer
    permission_classes = (IsOwner, )

    def get_queryset(self):
        # 해당 사용자의 가게 리스트만 보여준다.
        shop_list = Shop.objects.filter(owner=self.request.user.owner)
        return shop_list

    def perform_create(self, serializer):
        owner = self.request.user.owner
        shop_id = Shop.objects.filter(owner=owner).count() + 1 # 각 사장님별 가게들의 고유번호
        serializer.save(shop_id=shop_id, owner=owner)

class MyShopDetail(generics.RetrieveUpdateDestroyAPIView):
    # 해당 가게의 정보
    serializer_class = MyShopSerializer
    permission_classes = (IsOwner, )
    lookup_field = 'shop_id'

    def get_queryset(self):
        # 해당 사용자의 가게 리스트만 보여준다.
        shop_list = Shop.objects.filter(owner=self.request.user.owner)
        return shop_list

    def partial_update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)

class MenuList(generics.ListCreateAPIView):
    # 각 가게의 메뉴 리스트

    serializer_class = MenuSerializer
    permission_classes = (IsOwner, )

    def get_shop_insatnace(self):
        # 해당 유저의 해당 가게 인스턴스를 가져온다.
        shop_id = self.kwargs.get('shop_id')
        shop_owner = self.request.user.owner
        shop = get_object_or_404(Shop, shop_id=shop_id, owner=shop_owner)
        return shop

    def get_queryset(self):
        # 해당 가게의 메뉴 리스트만 가져온다.
        shop = self.get_shop_insatnace()
        is_sale = self.request.query_params.get('is_sale', False)
        menu_list = Menu.objects.filter(shop=shop, is_sale=is_sale)
        return menu_list

    def perform_create(self, serializer):
        shop = self.get_shop_insatnace()
        serializer.save(shop=shop)

class MenuDetail(generics.RetrieveUpdateDestroyAPIView):
    # 해당 메뉴의 정보
    serializer_class = MenuSerializer
    permission_classes = (IsOwner, )
    lookup_url_kwarg = 'menu_id'

    def get_shop_insatnace(self):
        # 해당 유저의 해당 가게 인스턴스를 가져온다.
        shop_id = self.kwargs.get('shop_id')
        shop_owner = self.request.user.owner
        shop = get_object_or_404(Shop, shop_id=shop_id, owner=shop_owner)
        return shop

    def get_queryset(self):
        # 해당 가게의 메뉴 리스트만 가져온다.
        shop = self.get_shop_insatnace()
        menu_list = Menu.objects.filter(shop=shop)
        return menu_list

    def partial_update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)

#-----------------------------------------------------------------------------------------

#MyShop 정보 생성
class MyShopCreateAPIView(CreateAPIView):
    queryset = Shop.objects.all()
    serializer_class = MyShopCreateUpdateSerializer
    #permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

#MyShop 정보 편집
class MyShopUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Shop.objects.all()
    serializer_class = MyShopCreateUpdateSerializer
    lookup_field = 'slug'
    permission_classes = [IsOwner] #사장이 자기 가게 정보만을 편집하게 함
    #lookup_url_kwarg = "abc"
    def perform_update(self, serializer):
        serializer.save(user=self.request.user)
        #email send_email

#가게 정보 삭제를 원하는 경우
class MyShopDeleteAPIView(DestroyAPIView):
    queryset = Shop.objects.all()
    serializer_class = MyShopDetailSerializer
    lookup_field = 'slug'
    permission_classes = [IsOwner] #사장이 자기 가게 정보만을 편집하게 함
    #lookup_url_kwarg = ""

#---------------------------------------------------------------------------------------

#Menu 정보 생성
class MenuCreateAPIView(CreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuCreateUpdateSerializer
    #permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

#Menu 정보 편집
class MenuUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Shop.objects.all()
    serializer_class = MenuCreateUpdateSerializer
    lookup_field = 'slug'
    permission_classes = [IsOwner] #사장이 자기 메뉴 정보만을 편집하게 함
    #lookup_url_kwarg = "abc"
    def perform_update(self, serializer):
        serializer.save(user=self.request.user)
        #email send_email

#Menu 정보 삭제를 원하는 경우
class MenuDeleteAPIView(DestroyAPIView):
    queryset = Shop.objects.all()
    serializer_class = MenuDetailSerializer
    lookup_field = 'slug'
    permission_classes = [IsOwner] #사장이 자기 메뉴 정보만을 편집하게 함
    #lookup_url_kwarg = ""




my_shop_list = MyShopList.as_view()
my_shop_detail = MyShopDetail.as_view()
menu_list = MenuList.as_view()
menu_detail = MenuDetail.as_view()
