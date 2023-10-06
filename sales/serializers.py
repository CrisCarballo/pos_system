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

    # 'total' es solo lectura porque se calcula
    extra_kwargs = {
        'total': {'read_only': True},
    }


class SaleDetailCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = SaleDetail
        fields = '__all__'


class SaleWithDetailsCreateSerializer(serializers.Serializer):
    sale = SaleCreateSerializer()
    sale_details = SaleDetailCreateSerializer(many=True)
