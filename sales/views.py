from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status

from sales.serializers import SaleCreateSerializer, SaleSerializer, SaleDetailSerializer
from sales.selectors import get_all_sales, get_sale_detail_by_id
from sales.services import create_sale, delete_sale


# Create your views here.

class GetSaleByIdAPI(APIView):
    def get(self, request):
        sale_id = request.query_params.get('id')
        sale_detail = get_sale_detail_by_id(sale_id)

        if sale_detail:
            serializer = SaleDetailSerializer(sale_detail)
            return Response(serializer.data)
        else:
            return Response({'error': 'No se encontró la venta'}, status=status.HTTP_404_NOT_FOUND)


class GetAllSalesAPI(APIView):
    def get(self, request):
        all_sales = get_all_sales()
        return Response(SaleSerializer(all_sales, many=True).data)


class CreateSaleAPI(APIView):
    class CreateSaleInputSerializer(serializers.Serializer):
        customer_id = serializers.IntegerField()  # proporcionar solamente el id
        sales_details = serializers.ListField()

    def post(self, request):
        serializer = self.CreateSaleInputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        if serializer.is_valid():
            return Response(SaleCreateSerializer(create_sale(
                **serializer.validated_data)).data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DeleteSaleAPI(APIView):
    class SaleInputSerializer(serializers.Serializer):
        id = serializers.IntegerField()

    def put(self, request):
        serializer = self.SaleInputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        return Response(
            SaleSerializer(delete_sale(
                **serializer.validated_data)).data
        )
