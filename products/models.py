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
        Category, on_delete=models.SET_NULL, null=True)
    price = models.FloatField()
    stock_quantity = models.PositiveBigIntegerField(default=0)
    created_at = models.DateField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        # Redondea el precio a 2 decimales antes de guardar
        self.price = round(self.price, 2)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name} {self.category} {self.price}"

    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"

'''
# category
{
    "id": "",
    "name": ""
}

# product
{
    "id": "",
    "name": "",
    "description": "",
    "category_id": "",
    "price": "",
    "stock_quantity": "",
    "is_active": "" # si es create, no pasar este param
}
'''