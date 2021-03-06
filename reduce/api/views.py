from django.shortcuts import get_object_or_404
from rest_framework import generics, filters
from api.permissions import IsCustomer
from api.serializers import ShopSerializer, MenuSerializer
from owner.models import Shop, Menu

class ShopList(generics.ListAPIView):
    # 위치를 통한 가게 리스트
    # ToDo: 위치 기반 기능 추가
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer
    permission_classes = (IsCustomer, )

class ShopDetail(generics.RetrieveAPIView):
    # 해당 가게의 정보
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer
    permission_classes = (IsCustomer, )
    lookup_url_kwarg = 'shop_id'

class MenuList(generics.ListAPIView):
    # 각 가게의 메뉴 리스트
    # ToDo: 해당 가게의 같은 메뉴 추가 안되게.
    serializer_class = MenuSerializer
    permission_classes = (IsCustomer, )

    def get_queryset(self):
        # 해당 가게의 메뉴 리스트만 가져온다.
        shop_id = self.kwargs.get('shop_id')
        shop = get_object_or_404(Shop, id=shop_id)
        is_sale = self.request.query_params.get('is_sale', False)
        menu_list = Menu.objects.filter(shop=shop, is_sale=is_sale)
        return menu_list

class MenuDetail(generics.RetrieveAPIView):
    # 해당 메뉴의 정보
    serializer_class = MenuSerializer
    permission_classes = (IsCustomer, )
    lookup_url_kwarg = 'menu_id'

    def get_queryset(self):
        # 해당 가게의 메뉴 리스트만 가져온다.
        shop_id = self.kwargs.get('shop_id')
        shop = get_object_or_404(Shop, id=shop_id)
        menu_list = Menu.objects.filter(shop=shop)
        return menu_list


shop_list = ShopList.as_view()
shop_detail = ShopDetail.as_view()
menu_list = MenuList.as_view()
menu_detail = MenuDetail.as_view()
