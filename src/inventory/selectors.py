from typing import Optional

from .models import Inventory
from .models import Product


def get_inventory_by_id_product(id:int) -> Optional[Inventory]:
    """
    La función `get_inventory_by_id_product` recupera el inventario de un producto en función de su ID.
    
    :param id: El parámetro "id" es un número entero que representa el ID del producto del que queremos
    recuperar el inventario
    :type id: int
    :return: una instancia del modelo de Inventario que coincide con la identificación dada, o Ninguno
    si el producto no existe o si hay un error al recuperar el inventario.
    """
    try:
        producto = Product.objects.get(id=id)
        inventory = Inventory.objects.filter(inventory__product=producto)
        return inventory
    except Product.DoesNotExist:
        return None
    except Exception as e:
        print(f"Error al obtener inventario: {str(e)}")
        return None