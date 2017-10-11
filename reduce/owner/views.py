from django.shortcuts import get_object_or_404
from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticated
from owner.models import Shop, Menu
from owner.serializers import ShopSerializer, MenuSerializer
from owner.permissions import IsOwner

class ShopList(generics.ListCreateAPIView):
    serializer_class = ShopSerializer
    permission_classes = (IsOwner, )

    def get_queryset(self):
        # 해당 사용자의 가게 리스트만 보여준다.
        shop_list = Shop.objects.filter(owner=self.request.user.owner)
        return shop_list

    def perform_create(self, serializer):
        owner = self.request.user.owner
        shop_id = Shop.objects.filter(owner=owner).count() + 1 # 각 사장님별 가게들의 고유번호
        serializer.save(shop_id=shop_id, owner=owner)

class ShopDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ShopSerializer
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
        is_sale = self.request.query_params.get('is_sale', False)
        menu_list = Menu.objects.filter(shop=shop, is_sale=is_sale)
        return menu_list

    def partial_update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)


shop_list = ShopList.as_view()
shop_detail = ShopDetail.as_view()
menu_list = MenuList.as_view()
menu_detail = MenuDetail.as_view()
