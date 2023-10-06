from rest_framework import serializers

from customers.serializers import CustomerSerializer
from products.serializers import ProductSerializer
from sales.models import Sale, SaleDetail


class SaleSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer()

    class Meta:
        model = Sale
        fields = '__all__'


class SaleDetailSerializer(serializers.ModelSerializer):
    sale = SaleSerializer()
    product = ProductSerializer()

    class Meta:
        model = SaleDetail
        fields = '__all__'


class SaleCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sale
        fields = '__all__'

    # 'total' y 'sale_number' son solo lectura porque se calculan
    extra_kwargs = {
        'total': {'read_only': True},
        'sale_number': {'read_only': True},
    }


class SaleDetailCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = SaleDetail
        fields = '__all__'
