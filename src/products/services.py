from typing import Optional
from src.inventory.services import update_inventory

from .models import Category, Product
from .selectors import get_category_by_id, get_product_by_id


# categories


def create_category(
        *,
        name: str
) -> Optional[Category]:
    """
    La función `create_category` crea una nueva categoria y la
    devuelve, o devuelve None si se produce un error.
    """
    try:
        category = Category.objects.create(
            name=name
        )
        return category
    except Exception as err:
        print(err)
        return None


def update_category(
        *,
        id: int,
        name: str
) -> Optional[Category]:
    """
    La función `update_category` edita una categoria y la
    devuelve, o devuelve None si se produce un error.
    """
    try:
        category = get_category_by_id(id)
        category.name = name
        category.save()
        return category
    except Exception as err:
        print(err)
        return None


def delete_category(id: int):
    """
    La función `delete_category` elimina un objeto de categoría según su ID.

    :param id: El parámetro "id" es un número entero que representa el identificador único de la
    categoría que debe eliminarse
    :type id: int
    """
    try:
        category = get_category_by_id(id)
        category.delete()
    except Exception as err:
        print(err)


# products


def create_product(
        *,
        name: str,
        description: str,
        category_id: int,
        price: float,
        stock_quantity: int
) -> Optional[Product]:
    """
    La función `create_product` crea un nuevo producto y lo
    devuelve, o devuelve None si se produce un error.
    """
    try:
        category = Category.objects.get(id=category_id)
        product = Product.objects.create(
            name=name,
            description=description,
            category=category,
            price=price,
            stock_quantity=stock_quantity
        )

        update_inventory(product, stock_quantity, 'entrada', f"Creación del producto: {product.name}")
        
        return product
    except Exception as err:
        print(err)
        return None


def update_product(
        *,
        id: int,
        name: str,
        description: str,
        category_id: int,
        price: float,
        stock_quantity: int,
        is_active: bool
) -> Optional[Product]:
    """
    La función `update_product` edita un product y lo
    devuelve, o devuelve None si se produce un error.
    """
    try:
        category = Category.objects.get(id=category_id)
        product = get_product_by_id(id)
        product.name = name
        product.description = description
        product.category = category
        product.price = price
        product.stock_quantity = stock_quantity
        product.is_active = is_active
        product.save()

        update_inventory(product, stock_quantity, 'entrada', f"Creación del producto: {product.name}")

        return product
    except Exception as err:
        print(err)
        return None


def delete_product(
        *,
        id: int
) -> Optional[Product]:
    """
    La función `delete_product` desactiva un producto estableciendo su atributo `is_active` en False y
    devuelve el producto desactivado.

    :param id: El parámetro "id" es un número entero que representa el identificador único del producto
    que debe eliminarse
    :type id: int
    :return: un objeto "Producto" si la eliminación se realizó correctamente, o "None" si hay un
    error.
    """
    try:
        product = get_product_by_id(id)
        product.is_active = False
        product.save()
        return product
    except Exception as err:
        print(err)
        return None
