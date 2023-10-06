from django.urls import path

from sales.views import CreateSaleAPI, DeleteSaleAPI, GetAllSalesAPI, GetSaleByIdAPI, GetSalesDetailsByIdCustomerAPI

urlpatterns = [
    path('get-sale/', GetSaleByIdAPI().as_view()),
    path('all-sales/', GetAllSalesAPI().as_view()),
    path('create-sale/', CreateSaleAPI().as_view()),
    path('delete-sale/', DeleteSaleAPI().as_view()),
    path('sales-datails-by-id-customer/', GetSalesDetailsByIdCustomerAPI().as_view()),
]
