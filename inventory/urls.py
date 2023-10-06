from django.urls import path

from inventory.views import GetInventoryByIdProductAPI


urlpatterns = [
    path('get-inventory-by-id-product/', GetInventoryByIdProductAPI().as_view()),
]
