from django.db import models

# Create your models here.


class Customer(models.Model):

    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    identification_number = models.CharField(
        max_length=20, blank=True, null=True)
    address = models.CharField(max_length=200, blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(max_length=50, blank=True, null=True)
    observations = models.TextField(blank=True, null=True)
    created_at = models.DateField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name} {self.lastName}"

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"

'''

{
    "name": "hola",
    "last_name": "hola",
    "identification_number": "123123",
    "address": "fjjfaafjop",
    "phone_number": "2456123",
    "email": "fjjfaafjop@cojaocj.com",
    "observations": "jfkasjaf"
}

'''


