from django.urls import path

from customers.views import CreateCustomerAPI, GetAllCustomersAPI

urlpatterns = [
    path('all/', GetAllCustomersAPI().as_view()),
    path('create/', CreateCustomerAPI().as_view())
]