
from typing import Iterable

from customers.models import Customer


def get_all_customers() -> Iterable[Customer]:
    try:
        return Customer.objects.all()
    except Exception as err:
        print(err)
