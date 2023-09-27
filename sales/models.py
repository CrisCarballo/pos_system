from django.db import models

from customers.models import Customer
from products.models import Product

# Create your models here.


class Sale(models.Model):
    sale_number = models.IntegerField(unique=True)
    customer = models.ForeignKey(
        Customer, on_delete=models.SET_NULL, null=True)
    total = models.DecimalField(max_digits=20, decimal_places=2, default=0.0)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.sale_number} {self.customer} {self.total} {self.date}"

    class Meta:
        verbose_name = "Venta"
        verbose_name_plural = "Ventas"


class SaleDetail(models.Model):
    sale = models.ForeignKey(Sale, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField()
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.product} {self.quantity} {self.unit_price}"

    class Meta:
        verbose_name = "Detalle de Venta"
        verbose_name_plural = "Detalles de Venta"
