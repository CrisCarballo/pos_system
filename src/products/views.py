from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers

from .serializers import CategorySerializer, ProductSerializer
from .selectors import get_all_categories, get_all_products, get_category_by_id, get_product_by_id
from .services import create_category, create_product, delete_category, delete_product, update_category, update_product


# Create your views here.


# categories

class GetCategoryByIdAPI(APIView):
    def get(self, request):
        id = request.query_params.get('id')
        category = get_category_by_id(id)
        return Response(ProductSerializer(category).data)


class GetAllCategoriesAPI(APIView):
    def get(self, request):
        all_categories = get_all_categories()
        return Response(CategorySerializer(all_categories, many=True).data)


class CreateCategoryAPI(APIView):
    class CategoryInputSerializer(serializers.Serializer):
        name = serializers.CharField()

    def post(self, request):
        serializer = self.CategoryInputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        return Response(
            CategorySerializer(create_category(
                **serializer.validated_data)).data
        )


class UpdateCategoryAPI(APIView):
    class CategoryInputSerializer(serializers.Serializer):
        id = serializers.IntegerField()
        name = serializers.CharField()

    def put(self, request):
        serializer = self.CategoryInputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        return Response(
            CategorySerializer(update_category(
                **serializer.validated_data)).data
        )


class DeleteCategoryAPI(APIView):

    def delete(self, request, id):

        return Response(
            delete_category(id)
        )


# products

class GetProductByIdAPI(APIView):
    def get(self, request):
        id = request.query_params.get('id')
        product = get_product_by_id(id)
        return Response(ProductSerializer(product).data)


class GetAllProductsAPI(APIView):
    def get(self, request):
        all_products = get_all_products()
        return Response(ProductSerializer(all_products, many=True).data)


class CreateProductAPI(APIView):
    class ProductInputSerializer(serializers.Serializer):
        name = serializers.CharField()
        description = serializers.CharField()
        category_id = serializers.IntegerField()  # proporcionar solamente el id
        price = serializers.FloatField()
        stock_quantity = serializers.IntegerField()

    def post(self, request):
        serializer = self.ProductInputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        return Response(
            ProductSerializer(create_product(
                **serializer.validated_data)).data
        )


class UpdateProductAPI(APIView):
    class ProductInputSerializer(serializers.Serializer):
        id = serializers.IntegerField()
        name = serializers.CharField()
        description = serializers.CharField()
        # proporcionar solamente el id para cambiar de categoria, no modifica la categoria en sí
        category_id = serializers.IntegerField()
        price = serializers.FloatField()
        stock_quantity = serializers.IntegerField()
        is_active = serializers.BooleanField()

    def put(self, request):
        serializer = self.ProductInputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        return Response(
            ProductSerializer(update_product(
                **serializer.validated_data)).data
        )


class DeleteProductAPI(APIView):
    class ProductInputSerializer(serializers.Serializer):
        id = serializers.IntegerField()

    def put(self, request):
        serializer = self.ProductInputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        return Response(
            ProductSerializer(delete_product(
                **serializer.validated_data)).data
        )
