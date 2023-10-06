
from typing import Iterable, Optional
from .models import Customer

from .models import Sale, SaleDetail


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


def get_sale_by_id(id: int) -> Sale:
    """
    La función `get_sale_by_id` recupera un objeto de venta de la base de datos en función de su ID y lo
    devuelve, o devuelve None si la venta no existe o se encuentran varias ventas con el mismo ID.

    :param id: El parámetro "id" es un número entero que representa el identificador único de una venta
    :type id: int
    :return: una instancia del modelo Venta si existe y no es None. Si la Venta no existe o se
    devuelven varias instancias, devolverá Ninguna.
    """
    try:
        sale = Sale.objects.get(id=id)
        if Sale is not None:
            return sale
    except (Sale.DoesNotExist, Sale.MultipleObjectsReturned) as err:
        print(err)
        return None


def get_all_sales() -> Iterable[Sale]:
    """
    La función `get_all_sales` recupera todos los objetos de ventas de la base de datos y los devuelve
    como un iterable.
    :return: todos los objetos de Venta.
    """
    try:
        return Sale.objects.all()
    except Exception as err:
        print(err)


def get_sales_details_by_id_customer(id:int) -> Optional[Iterable[SaleDetail]]:
    """
    La función recupera detalles de ventas de un cliente con una identificación determinada.
    
    :param id: El parámetro "id" es un número entero que representa el ID de un cliente
    :type id: int
    :return: una colección de objetos SaleDetail que están asociados con un cliente específico.
    """
    try:
        customer = Customer.objects.get(id=id)
        sales_details = SaleDetail.objects.filter(sale__customer=customer)
        return sales_details
    except Customer.DoesNotExist:
        return None
    except Exception as e:
        print(f"Error al obtener detalles de venta: {str(e)}")
        return None