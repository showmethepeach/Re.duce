from django.shortcuts import get_object_or_404
from rest_framework import status, generics, filters
from rest_framework.response import Response
from api.permissions import IsCustomer, IsReviewWriter, IsOrderer
from api.serializers import ShopSerializer, MenuSerializer, ReviewSerializer, OrderSerializer, OrderSaleMenuSerializer
from api.models import Review
from owner.models import Shop, Menu, Order, OrderSaleMenu


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

class ReviewList(generics.ListCreateAPIView):
    # 해당 가게의 리뷰 리스트

    serializer_class = ReviewSerializer
    permission_classes = (IsCustomer, )

    def get_shop_instance(self):
        shop_id = self.kwargs.get('shop_id')
        return get_object_or_404(Shop, id=shop_id)

    def get_queryset(self):
        # 해당 가게의 리뷰 리스트만 가져온다.
        shop = self.get_shop_instance()
        review_list = Review.objects.filter(shop=shop)
        return review_list

    def create(self, request, *args, **kwargs):
        # 주문 정보가 있는 사람만 작성 가능
        customer = request.user.customer
        shop = self.get_shop_instance()
        if customer.order_set.filter(shop=shop).exists():
            # 해당가게에 주문 정보가 있을 경우
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save(customer=customer, shop=shop)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)

class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    # 해당 메뉴의 정보
    serializer_class = ReviewSerializer
    permission_classes = (IsCustomer, IsReviewWriter, )
    lookup_url_kwarg = 'review_id'

    def get_shop_instance(self):
        shop_id = self.kwargs.get('shop_id')
        return get_object_or_404(Shop, id=shop_id)

    def get_queryset(self):
        # 해당 가게의 리뷰 리스트만 가져온다.
        shop = self.get_shop_instance()
        review_list = Review.objects.filter(shop=shop)
        return review_list

    def partial_update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)

class OrderList(generics.ListCreateAPIView):
    # 주문 내역 리스트

    serializer_class = OrderSerializer
    permission_classes = (IsCustomer, )

    def get_shop_instance(self):
        shop_id = self.kwargs.get('shop_id')
        return get_object_or_404(Shop, id=shop_id)

    def get_queryset(self):
        # 나의 주문 리스트를 가져온다.
        customer = self.request.user.customer
        order_list = Order.objects.filter(customer=customer)
        return order_list

    def perform_create(self, serializer):
        customer = self.request.user.customer
        shop = self.get_shop_instance()
        serializer.save(customer=customer, shop=shop)

class OrderDetail(generics.RetrieveAPIView):
    # 해당 주문의 메뉴정보
    serializer_class = OrderSerializer
    permission_classes = (IsCustomer, IsOrderer)
    lookup_url_kwarg = 'order_id'

    def get_shop_instance(self):
        shop_id = self.kwargs.get('shop_id')
        return get_object_or_404(Shop, id=shop_id)

    def get_queryset(self):
        # 나의 주문 리스트를 가져온다.
        customer = self.request.user.customer
        order_list = Order.objects.filter(customer=customer)
        return order_list


shop_list = ShopList.as_view()
shop_detail = ShopDetail.as_view()
menu_list = MenuList.as_view()
menu_detail = MenuDetail.as_view()
review_list = ReviewList.as_view()
review_detail = ReviewDetail.as_view()
order_list = OrderList.as_view()
order_detail = OrderDetail.as_view()
