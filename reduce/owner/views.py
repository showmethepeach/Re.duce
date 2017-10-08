from rest_framework import generics
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
        serializer.save(owner=self.request.user.owner)

class ShopDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ShopSerializer
    permission_classes = (
        IsOwner, )
    lookup_field = 'name'

    def get_queryset(self):
        # 해당 사용자의 가게 리스트만 보여준다.
        shop_list = Shop.objects.filter(owner=self.request.user.owner)
        return shop_list

    def partial_update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)


shop_list = ShopList.as_view()
shop_detail = ShopDetail.as_view()
