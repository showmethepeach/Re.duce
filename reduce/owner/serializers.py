from rest_framework import serializers
from owner.models import Shop, Menu


class ShopSerializer(serializers.ModelSerializer):

    class Meta:
        model = Shop
        fields = ('owner', 'name', 'description', 'business_number', 'contact_number', 'address')
        extra_kwargs = {'owner': {'read_only': True}}


class MenuSerializer(serializers.ModelSerializer):

    class Meta:
        Model = Menu
        fields = ('name', 'price', 'description', 'is_sale', 'sale_rate', )
