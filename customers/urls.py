from django.urls import path

from customers.views import CreateCustomerAPI, GetAllCustomersAPI, GetCustomerByIdAPI, UpdateCustomerAPI

urlpatterns = [
    path('<int:id>/', GetCustomerByIdAPI().as_view()),
    path('all/', GetAllCustomersAPI().as_view()),
    path('create/', CreateCustomerAPI().as_view()),
    path('update/', UpdateCustomerAPI().as_view()),
    path('delete/', UpdateCustomerAPI().as_view()),
]