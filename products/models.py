from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "Categoría"
        verbose_name_plural = "Categorías"


class Product(models.Model):

    name = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)
    category = models.ForeignKey(
        Category, on_delete=models.DO_NOTHING, null=True)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    stock_quantity = models.PositiveBigIntegerField(default=0)
    created_at = models.DateField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name} {self.category} {self.price}"

    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"
