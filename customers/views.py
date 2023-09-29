from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework.pagination import PageNumberPagination
from customers.selectors import get_all_customers

from customers.serializers import CustomerSerializer
from customers.services import create_customer

# Create your views here.


class GetAllCustomersAPI(APIView):
    def get(self, request):
        all_customers = get_all_customers()
        return Response(CustomerSerializer(all_customers, many=True).data)


class CreateCustomerAPI(APIView):
    class CustomerInputSerializer(serializers.Serializer):
        name = serializers.CharField()
        last_name = serializers.CharField()
        identification_number = serializers.IntegerField()
        address = serializers.CharField()
        phone_number = serializers.CharField()
        email = serializers.EmailField()
        observations = serializers.CharField()

    def post(self, request):
        serializer = self.CustomerInputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        return Response(
            CustomerSerializer(create_customer(
                **serializer.validated_data)).data
        )
