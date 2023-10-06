from django.urls import path

from sales.views import CreateSaleAPI, DeleteSaleAPI, GetAllSalesAPI, GetSaleByIdAPI

urlpatterns = [
    path('get-sale/', GetSaleByIdAPI().as_view()),
    path('all-sales/', GetAllSalesAPI().as_view()),
    path('create-sale/', CreateSaleAPI().as_view()),
    path('delete-sale/', DeleteSaleAPI().as_view()),
]
