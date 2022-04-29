from rest_framework import serializers

from webapp.models import Shop, Good


class GoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Good
        fields = "__all__"


class ShopWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = "__all__"


class ShopReadSerializer(serializers.ModelSerializer):
    good = GoodSerializer(many=True, required=False)

    class Meta:
        model = Shop
        fields = "__all__"
