from django.urls import path

from products.views import CreateCategoryAPI, CreateProductAPI, DeleteCategoryAPI, DeleteProductAPI, GetAllCategoriesAPI, GetAllProductsAPI, GetCategoryByIdAPI, GetProductByIdAPI, UpdateCategoryAPI, UpdateProductAPI

urlpatterns = [
    # categories
    path('get-category/', GetCategoryByIdAPI().as_view()),
    path('all-categories/', GetAllCategoriesAPI().as_view()),
    path('create-category/', CreateCategoryAPI().as_view()),
    path('update-category/', UpdateCategoryAPI().as_view()),
    path('delete-category/<int:id>/', DeleteCategoryAPI().as_view()),
    # products
    path('get-product/', GetProductByIdAPI().as_view()),
    path('all-products/', GetAllProductsAPI().as_view()),
    path('create-product/', CreateProductAPI().as_view()),
    path('update-product/', UpdateProductAPI().as_view()),
    path('delete-product/', DeleteProductAPI().as_view()),
]
