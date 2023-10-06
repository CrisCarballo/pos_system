from rest_framework import serializers
from inventory.models import Inventory

from products.serializers import ProductSerializer


class InventorySerializer(serializers.ModelSerializer):

    product = ProductSerializer()

    class Meta:
        model = Inventory
        fields = '__all__'