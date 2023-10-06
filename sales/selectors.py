
from typing import Iterable

from sales.models import SaleDetail


def get_all_sales_with_detail() -> Iterable[SaleDetail]:
    """
    La función `get_all_sales_with_detail` recupera todas las ventas de la base de datos y los devuelve como
    un iterable.
    :return: todas las ventas como un iterable de objetos SaleDetail.
    """
    try:
        return SaleDetail.objects.all()
    except Exception as err:
        print(err)


def get_sale_detail_by_id(id: int) -> SaleDetail:
    """
    La función `get_sale_detail_by_id` recupera un objeto de SaleDetail de la base de datos en función del ID
    de sale proporcionado.

    :param id: El parámetro `id` es un número entero que representa el ID de la venta
    que desea recuperar
    :type id: int
    :return: una instancia del modelo SaleDetail si se encuentra una venta con el ID especificado. Si no
    se encuentra ningúna venta o si se encuentran varias ventas con el mismo ID, la función devuelve
    None.
    """
    try:
        sale_detail = SaleDetail.objects.get(id=id)
        if SaleDetail is not None:
            return sale_detail
    except (SaleDetail.DoesNotExist, SaleDetail.MultipleObjectsReturned) as err:
        print(err)
        return None