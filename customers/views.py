from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework.pagination import PageNumberPagination
from customers.selectors import get_all_customers, get_customer_by_id

from customers.serializers import CustomerSerializer
from customers.services import create_customer, delete_customer, update_customer

# Create your views here.

class GetCustomerByIdAPI(APIView):
    def get(self, request, id_customer):
        customer = get_customer_by_id(id_customer)
        return Response(CustomerSerializer(customer).data)


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


class UpdateCustomerAPI(APIView):
    class CustomerInputSerializer(serializers.Serializer):
        id_customer = serializers.IntegerField()
        name = serializers.CharField()
        last_name = serializers.CharField()
        identification_number = serializers.IntegerField()
        address = serializers.CharField()
        phone_number = serializers.CharField()
        email = serializers.EmailField()
        observations = serializers.CharField()


    def put(self, request):
        serializer = self.CustomerInputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        return Response(
            CustomerSerializer(update_customer(
                **serializer.validated_data)).data
        )
    

class DeleteCustomerAPI(APIView):
    def put(self, request):
        id_customer = request.query_params.get("id_customer")
        return Response(
            delete_customer(id_customer)
        )