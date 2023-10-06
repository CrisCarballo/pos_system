from django.db import models

from src.customers.models import Customer
from src.products.models import Product

# Create your models here.


class Sale(models.Model):
    sale_number = models.IntegerField(unique=True)
    customer = models.ForeignKey(
        Customer, on_delete=models.SET_NULL, null=True)
    total = models.FloatField(default=0)
    date = models.DateField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        # Redondea el total a 2 decimales antes de guardar
        self.total = round(self.total, 2)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.sale_number} {self.customer} {self.total} {self.date}"

    class Meta:
        verbose_name = "Venta"
        verbose_name_plural = "Ventas"

    def get_total(self) -> float:
        """
        La función calcula el total sumando los subtotales de todos los detalles de venta asociados con
        una venta.
        :return: la suma total de los subtotales de todos los detalles de la venta en saledetail_set.
        """
        total = sum([sale_detail.get_subtotal()
                    for sale_detail in self.sale_detail_set.all()])
        return total


class SaleDetail(models.Model):
    sale = models.ForeignKey(
        Sale, on_delete=models.SET_NULL, null=True, related_name='sale_detail_set')
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    quantity = models.PositiveIntegerField(default=0)
    unit_price = models.FloatField(default=0)
    is_active = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        # Redondea el precio unitario a 2 decimales antes de guardar
        self.unit_price = round(self.unit_price, 2)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.product} {self.quantity} {self.unit_price}"

    class Meta:
        verbose_name = "Detalle de Venta"
        verbose_name_plural = "Detalles de Venta"

    def get_subtotal(self) -> float:
        """
        La función calcula el subtotal multiplicando la cantidad y el precio unitario.
        :return: el subtotal, que es el producto de la cantidad y el precio unitario.
        """
        subtotal = self.quantity * self.unit_price
        return subtotal


'''
{
  "customer_id": "1", 
  "sales_details": [
    {
      "product": "1",
      "quantity": "3",
      "unit_price": "5.99"
    },
    {
      "product": "2",
      "quantity": "1",
      "unit_price": "50"
    },
    {
      "product": "3",
      "quantity": "10",
      "unit_price": "20.00"
    }
  ]
}
'''
