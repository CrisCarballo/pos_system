from django.db import models
from django.core.validators import MinValueValidator

from products.models import Product

# Create your models here.


class Inventory(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    quantity = models.PositiveIntegerField(
        validators=[MinValueValidator(1)])
    TRANSACTION_CHOICES = (
        ('entrada', 'Entrada'),
        ('salida', 'Salida'),
    )
    transaction_type = models.CharField(
        max_length=20, choices=TRANSACTION_CHOICES)
    transaction_date = models.DateTimeField(auto_now_add=True)
    notes = models.CharField(max_length=200, null=True, default="")

    def __str__(self):
        return f"{self.product.name} {self.quantity} {self.transaction_date}"


    class Meta:
        verbose_name = "Inventario"
        verbose_name_plural = "Inventarios"

    def set_increase_quantity(self, quantity):
        """
        La función aumenta la cantidad de un producto en el inventario y guarda los cambios.
        
        :param quantity: El parámetro quantity es la cantidad en la que desea aumentar el valor de
        cantidad actual
        """
        self.quantity += quantity
        self.save()

    def set_decrease_quantity(self, quantity):
        """
        La función disminuye la cantidad de un producto en el inventario y guarda el valor actualizado,
        pero genera un error si la cantidad cae por debajo de cero.
        
        :param quantity: El parámetro quantity representa la cantidad en la que se debe disminuir la
        cantidad de un producto
        """
        if self.quantity >= quantity:
            self.quantity -= quantity
            self.save()
        else:
            raise ValueError("No se puede disminuir la cantidad por debajo de cero.")