from rest_framework import serializers
from owner.models import Shop, Menu, Order, OrderSaleMenu


class MyShopSerializer(serializers.ModelSerializer):

    class Meta:
        model = Shop
        fields = ('id', 'shop_id', 'owner', 'name', 'description', 'business_number', 'contact_number', 'address', 'image')
        extra_kwargs = {
            'id': {'read_only': True},
            'owner': {'read_only': True},
            'shop_id': {'read_only': True},
            }


class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ('id', 'shop', 'name', 'price', 'description', 'is_sale', 'sale_rate', 'image')
        extra_kwargs = {
            'id': {'read_only': True},
            'shop': {'read_only': True},
            'image': {'use_url': True},
        }

class OrderSaleMenuSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrderSaleMenu
        fields = ('menu', 'quantity', )

class OrderSerializer(serializers.ModelSerializer):
    order_sale_menus = OrderSaleMenuSerializer(many=True)

    class Meta:
        model = Order
        fields = ('customer', 'shop', 'is_finished', 'total_price', 'ordered_at', 'order_sale_menus')
        extra_kwargs = {
            'ordered_at': {'read_only': True},
            'customer': {'read_only': True},
            'shop': {'read_only': True},
        }
