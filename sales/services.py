from typing import Iterable, Optional
from django.db import transaction
from django.db.models import Max

from customers.models import Customer
from inventory.models import Inventory
from inventory.services import update_inventory
from products.models import Product
from sales.models import Sale, SaleDetail
from sales.selectors import get_sale_by_id


def create_sale(
        customer_id: int,
        sales_details: Iterable[SaleDetail]
) -> Sale:
    """
    La función `create_sale` crea un nuevo registro de venta en la base de datos con el ID del cliente y
    los detalles de ventas proporcionados, incluido el número de venta, el cliente, el total y los
    detalles de venta asociados.

    :param customer_id: El parámetro `customer_id` es un número entero que representa el ID del cliente
    para quien se crea la venta. Esta ID se utiliza para recuperar el objeto del cliente de la base de
    datos
    :type customer_id: int
    :param sales_details: El parámetro `sales_details` es un diccionario que contiene los detalles de la
    venta. Cada detalle consta de la siguiente información:
    :type sales_details: dict[SaleDetail]
    :return: una instancia del modelo Sale, que representa una venta en el sistema.
    """
    try:
        with transaction.atomic():

            # Obtener el valor máximo de sale_number si hay registros existentes
            max_sale_number = Sale.objects.aggregate(Max('sale_number'))[
                'sale_number__max']

            # Si no hay registros previos, asignar 1 como el nuevo valor de sale_number
            new_sale_number = (max_sale_number or 0) + 1

            # Obtiene el cliente con el parametro customer_id
            customer = Customer.objects.get(id=customer_id)

            # Calcula el total sumando los subtotales de los detalles de venta
            total = 0.00
            for detail in sales_details:
                total += float(detail['quantity']) * \
                    float(detail['unit_price'])

            # Crea la venta principal en la base de datos
            sale = Sale.objects.create(
                sale_number=new_sale_number,
                customer=customer,
                total=total
            )

            # Crea los detalles de venta asociados a la venta principal
            for detail_data in sales_details:
                product = Product.objects.get(pk=detail_data['product'])
                SaleDetail.objects.create(
                    sale=sale,
                    product=product,
                    quantity=float(detail_data['quantity']),
                    unit_price=float(detail_data['unit_price'])
                )

            # Actualiza el inventario disminuyendo la cantidad vendida
                inventory_entry = Inventory.objects.filter(
                    product=product).first()

                if inventory_entry:
                    inventory_entry.set_decrease_quantity(
                        float(detail_data['quantity']))
                else:
                    raise ValueError(
                        f"Producto no encontrado en el inventario: {product.name}")

            return sale
    except Exception as e:
        print(f"Error en la creación de la venta: {str(e)}")
        raise  # Re-lanzar la excepción para que sea manejada en la vista o donde sea necesario


def delete_sale(
        *,
        id: int
) -> Optional[Sale]:
    """
    La función `delete_sale` elimina una venta estableciendo su atributo `is_active` en False y
    guardando los cambios.
    
    :param id: El parámetro "id" es un número entero que representa el identificador único de la venta
    que debe eliminarse
    :type id: int
    :return: un objeto Venta si la venta se elimina correctamente, o Ninguno si hay un error.
    """
    try:
        sale = get_sale_by_id(id)
        sale.is_active = False
        sale.save()

        sales_details = SaleDetail.objects.filter(sale=sale)

        # Actualizo el inventario de cada producto de la venta eliminada
        for sale_detail in sales_details:
            product = sale_detail.product
            quantity = sale_detail.quantity
            update_inventory(product, quantity, 'entrada', f"Por venta N°-{sale.sale_number} cancelada")

        return sale
    except Exception as err:
        print(err)
        return None
