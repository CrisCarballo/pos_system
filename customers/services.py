import datetime
from typing import Optional

from customers.models import Customer
from customers.selectors import get_customer_by_id


def create_customer(
        *,
        name: str,
        last_name: str,
        identification_number: int,
        address: str,
        phone_number: str,
        email: str,
        observations: str
) -> Optional[Customer]:
    """
    La función `create_customer` crea un nuevo customer y lo
    devuelve, o devuelve None si se produce un error.
    """
    try:
        customer = Customer.objects.create(
            name=name,
            last_name=last_name,
            identification_number=identification_number,
            address=address,
            phone_number=phone_number,
            email=email,
            observations=observations
        )
        return customer
    except Exception as err:
        print(err)
        return None


def update_customer(
        *,
        id_customer: int,
        name: str,
        last_name: str,
        identification_number: int,
        address: str,
        phone_number: str,
        email: str,
        observations: str
) -> Optional[Customer]:
    """
    La función `update_customer` edita un customer y lo
    devuelve, o devuelve None si se produce un error.
    """
    try:
        customer = get_customer_by_id(id_customer)
        customer.name = name,
        customer.last_name = last_name,
        customer.identification_number = identification_number,
        customer.address = address,
        customer.phone_number = phone_number,
        customer.email = email,
        customer.observations = observations
        customer.save()
        return customer
    except Exception as err:
        print(err)
        return None


def delete_customer(id_customer: int) -> Optional[Customer]:
    """
    La función `delete_customer` toma un `id_customer` como entrada, recupera el cliente con ese ID,
    establece su atributo `is_active` en False, guarda los cambios y devuelve el objeto del cliente.
    
    :param id_customer: El parámetro `id_customer` es un número entero que representa el identificador
    único de un cliente
    :type id_customer: int
    :return: una instancia de la clase Cliente si el cliente se elimina correctamente, o None si hay
    un error.
    """
    try:
        customer = get_customer_by_id(id_customer)
        customer.is_active = False
        customer.save()
        return customer
    except Exception as err:
        print(err)
        return None