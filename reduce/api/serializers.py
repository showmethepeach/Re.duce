from django.db import transaction
from rest_framework import serializers
from owner.models import Shop, Menu, Order, OrderSaleMenu
from api.models import Review

# Todo 모든 시리얼라이저 필요없는 필드 지우기
class ShopSerializer(serializers.ModelSerializer):

    class Meta:
        model = Shop
        fields = ('id', 'name', 'description', 'contact_number', 'address', 'image')

class MenuSerializer(serializers.ModelSerializer):

    class Meta:
        model = Menu
        fields = ('id', 'shop', 'name', 'price', 'description', 'is_sale', 'sale_rate', 'image')
        extra_kwargs = {
            'id': {'read_only': True},
            'shop': {'read_only': True},
        }

class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = ('customer', 'shop', 'content', 'rating', )
        extra_kwargs = {
            'customer': {'read_only': True},
            'shop': {'read_only': True},
        }

class OrderSaleMenuSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrderSaleMenu
        fields = ('menu', 'quantity', )

class OrderSerializer(serializers.ModelSerializer):
    order_sale_menus = OrderSaleMenuSerializer(many=True)

    class Meta:
        model = Order
        fields = ('customer', 'shop', 'total_price', 'ordered_at', 'order_sale_menus')
        extra_kwargs = {
            'ordered_at': {'read_only': True},
            'customer': {'read_only': True},
            'shop': {'read_only': True},
        }

    def create(self, validated_data):
        ordered_menu_data = validated_data.pop('order_sale_menus')

        with transaction.atomic():
            # transaction all or nothing
            order = Order.objects.create(**validated_data)
            for ordered_menu in ordered_menu_data:
                # if ordered_menu['menu'] in order.shop.menu_set.all():
                OrderSaleMenu.objects.create(order=order, **ordered_menu)
            return order

