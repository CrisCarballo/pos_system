
from typing import Iterable

from customers.models import Customer


def get_all_customers() -> Iterable[Customer]:
    """
    La función `get_all_customers` recupera todos los clientes de la base de datos y los devuelve como
    un iterable.
    :return: todos los clientes como un iterable de objetos Cliente.
    """
    try:
        return Customer.objects.all()
    except Exception as err:
        print(err)


def get_customer_by_id(id: int) -> Customer:
    """
    La función `get_customer_by_id` recupera un objeto de cliente de la base de datos en función del ID
    de cliente proporcionado.

    :param id: El parámetro `id` es un número entero que representa el ID del cliente
    que desea recuperar
    :type id: int
    :return: una instancia del modelo Cliente si se encuentra un cliente con el ID especificado. Si no
    se encuentra ningún cliente o si se encuentran varios clientes con el mismo ID, la función devuelve
    None.
    """
    try:
        customer = Customer.objects.get(id=id)
        if customer is not None:
            return customer
    except (Customer.DoesNotExist, Customer.MultipleObjectsReturned) as err:
        print(err)
        return None
