from django.urls import path

from .views import CreateCustomerAPI, DeleteCustomerAPI, GetAllCustomersAPI, GetCustomerByIdAPI, UpdateCustomerAPI

urlpatterns = [
    path('get-customer/', GetCustomerByIdAPI().as_view()),
    path('all/', GetAllCustomersAPI().as_view()),
    path('create/', CreateCustomerAPI().as_view()),
    path('update/', UpdateCustomerAPI().as_view()),
    path('delete/', DeleteCustomerAPI().as_view()),
]
