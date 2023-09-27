import datetime
from typing import Optional

from customers.models import Customer


def create_customer(
        *,
        name: str,
        last_name: str,
        identification_number: int,
        address: str,
        phone_number: str,
        email: str,
        observations: str,
        created_at: datetime.date,
        is_active: bool
) -> Optional[Customer]:
    """
    La función `create_customer` crea un nuevo objeto de customer y lo
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
            observations=observations,
            created_at=created_at,
            is_active=is_active
        )
        return customer
    except Exception as err:
        print(err)
        return None
