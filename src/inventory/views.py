from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from .selectors import get_inventory_by_id_product
from .serializers import InventorySerializer

# Create your views here.


class GetInventoryByIdProductAPI(APIView):
    def get(self, request):
        product_id = request.query_params.get('id')
        inventory = get_inventory_by_id_product(product_id)
        return Response(InventorySerializer(inventory, many=True).data)