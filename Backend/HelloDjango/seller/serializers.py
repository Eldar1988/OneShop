from rest_framework import serializers

from .models import Tariff, Seller, Shop


class TariffSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tariff
        exclude = ('order',)


class SellerSerializer(serializers.ModelSerializer):
    tariff = TariffSerializer(many=False)

    class Meta:
        model = Seller
        exclude = ('updated',)


class ShopSerializer(serializers.ModelSerializer):

    class Meta:
        model = Shop
        fields = '__all__'
