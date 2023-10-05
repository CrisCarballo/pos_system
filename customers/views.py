from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers

from customers.serializers import CustomerSerializer
from customers.selectors import get_all_customers, get_customer_by_id
from customers.services import create_customer, delete_customer, update_customer

# Create your views here.


class GetCustomerByIdAPI(APIView):
    def get(self, request):
        id = request.query_params.get('id')
        customer = get_customer_by_id(id)
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
        id = serializers.IntegerField()
        name = serializers.CharField()
        last_name = serializers.CharField()
        identification_number = serializers.IntegerField()
        address = serializers.CharField()
        phone_number = serializers.CharField()
        email = serializers.EmailField()
        observations = serializers.CharField()
        is_active = serializers.BooleanField()

    def put(self, request):
        serializer = self.CustomerInputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        return Response(
            CustomerSerializer(update_customer(
                **serializer.validated_data)).data
        )


class DeleteCustomerAPI(APIView):
    class CustomerInputSerializer(serializers.Serializer):
        id = serializers.IntegerField()

    def put(self, request):
        serializer = self.CustomerInputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        return Response(
            CustomerSerializer(delete_customer(
                **serializer.validated_data)).data
        )
