from typing import Optional
from django.db import transaction
from customers.models import Customer

from products.models import Product
from sales.models import Sale, SaleDetail
from sales.selectors import get_sale_by_id


def create_sale(customer: Customer, sale_details: dict[SaleDetail]) -> Sale:
    """
    La función `create_sale` crea un registro de venta en la base de datos con el cliente dado y los
    detalles de la venta, incluido el monto total, y devuelve el objeto de venta creado.
    
    :param customer: El parámetro "cliente" es una instancia de la clase de modelo "Cliente". Representa
    al cliente que realizó la venta
    :type customer: Customer
    :param sale_details: El parámetro `sale_details` es un diccionario que contiene los detalles de la
    venta. Cada detalle está representado por un diccionario con las siguientes claves:
    :type sale_details: dict[SaleDetail]
    :return: una instancia del modelo de Sale.
    """
    try:
        with transaction.atomic():
            # Calcula el total sumando los subtotales de los detalles de venta
            total = 0.00
            for detail in sale_details:
                total += float(detail['quantity']) * float(detail['unit_price'])

            # Crea la venta principal en la base de datos
            sale = Sale.objects.create(customer=customer, total=total)

            # Crea los detalles de venta asociados a la venta principal
            for detail_data in sale_details:
                product = Product.objects.get(pk=detail_data['product'])
                SaleDetail.objects.create(
                    sale=sale,
                    product=product,
                    quantity=float(detail_data['quantity']),
                    unit_price=float(detail_data['unit_price'])
                )

            return sale
    except Exception as e:
        print(f"Error en la creación de la venta: {str(e)}")
        raise  # Re-lanzar la excepción para que sea manejada en la vista o donde sea necesario

