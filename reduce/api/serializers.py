from rest_framework import serializers
from owner.models import Shop, Menu
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
