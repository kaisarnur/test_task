from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action

from webapp.models import Good, Shop
from api.serializers import ShopReadSerializer, ShopWriteSerializer


class ShopViewSet(ModelViewSet):
    queryset = Shop.objects.all()
    serializer_class = ShopWriteSerializer

    def get_serializer_class(self):
        if self.action in ("list", "retrieve"):
            return ShopReadSerializer
        return self.serializer_class

    @action(detail=True, methods=["GET"], url_path="goods", url_name="goods")
    def get_shop_goods(self, request, *args, **kwargs):
        shop_pk = kwargs["pk"]
        goods = Good.objects.filter(shop_id=shop_pk).values("id", "name")
        return Response(goods)
