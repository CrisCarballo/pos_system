from django.urls import path

from .views import GetInventoryByIdProductAPI


urlpatterns = [
    path('get-inventory-by-id-product/', GetInventoryByIdProductAPI().as_view()),
]
