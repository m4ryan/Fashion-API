from rest_framework import serializers
from .models import Merchant, FashionProduct

class MerchantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Merchant
        fields = '__all__'

class FashionProductSerializer(serializers.ModelSerializer):
    merchant = serializers.PrimaryKeyRelatedField(queryset=Merchant.objects.all())

    class Meta:
        model = FashionProduct
        fields = '__all__'
