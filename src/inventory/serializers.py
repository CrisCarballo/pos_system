from rest_framework import serializers

from .models import Inventory
from src.products.serializers import ProductSerializer


class InventorySerializer(serializers.ModelSerializer):

    product = ProductSerializer()

    class Meta:
        model = Inventory
        fields = '__all__'