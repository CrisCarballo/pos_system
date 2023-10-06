from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status

from sales.serializers import SaleCreateSerializer, SaleSerializer, SaleDetailSerializer
from sales.selectors import get_all_sales_with_detail, get_sale_detail_by_id
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
        all_sales = get_all_sales_with_detail()
        return Response(SaleSerializer(all_sales, many=True).data)


class CreateSaleAPI(APIView):
    def post(self, request):
        serializer = SaleCreateSerializer(data=request.data)

        if serializer.is_valid():
            customer = serializer.validated_data['customer']
            sale_details = serializer.validated_data['sale_details']

            # Llama a la función del servicio para crear la venta con detalles
            sale = create_sale(customer, sale_details)

            return Response({'message': 'Sale created successfully', 'sale_id': sale.id}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
