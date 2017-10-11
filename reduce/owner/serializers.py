from rest_framework import serializers
from owner.models import Shop, Menu


class MyShopSerializer(serializers.ModelSerializer):

    class Meta:
        model = Shop
        fields = ('id', 'shop_id', 'owner', 'name', 'description', 'business_number', 'contact_number', 'address')
        extra_kwargs = {
            'id': {'read_only': True},
            'owner': {'read_only': True},
            'shop_id': {'read_only': True},
            }


class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ('id', 'shop', 'name', 'price', 'description', 'is_sale', 'sale_rate', )
        extra_kwargs = {
            'id': {'read_only': True},
            'shop': {'read_only': True},
        }
