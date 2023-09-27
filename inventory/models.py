from django.db import models

from products.models import Product

# Create your models here.


class Inventory(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    quantity = models.PositiveIntegerField()
    entry_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.product.name} {self.quantity} {self.entry_date}"
