
from typing import Iterable

from products.models import Product, Category

# categories


def get_all_categories() -> Iterable[Category]:
    """
    La función `get_all_categories` recupera todas las categories de la base de datos y los devuelve como
    un iterable.
    :return: todas las categories como un iterable de objetos Category.
    """
    try:
        return Category.objects.all()
    except Exception as err:
        print(err)


def get_category_by_id(id: int) -> Category:
    """
    La función `get_category_by_id` recupera un objeto de category de la base de datos en función del ID
    de category proporcionado.

    :param id: El parámetro `id` es un número entero que representa el ID de la categoria
    que desea recuperar
    :type id: int
    :return: una instancia del modelo Category si se encuentra una categoria con el ID especificado. Si no
    se encuentra ningúna categoria o si se encuentran varias categorias con el mismo ID, la función devuelve
    None.
    """
    try:
        category = Category.objects.get(id=id)
        if Category is not None:
            return category
    except (Category.DoesNotExist, Category.MultipleObjectsReturned) as err:
        print(err)
        return None


# products

def get_all_products() -> Iterable[Product]:
    """
    La función `get_all_products` recupera todos los productos de la base de datos y los devuelve como
    un iterable.
    :return: todos los productos como un iterable de objetos Products.
    """
    try:
        return Product.objects.all()
    except Exception as err:
        print(err)


def get_product_by_id(id: int) -> Product:
    """
    La función `get_product_by_id` recupera un objeto de producto de la base de datos en función del ID
    de producto proporcionado.

    :param id: El parámetro `id` es un número entero que representa el ID del producto
    que desea recuperar
    :type id: int
    :return: una instancia del modelo Producto si se encuentra un producto con el ID especificado. Si no
    se encuentra ningún producto o si se encuentran varios productos con el mismo ID, la función devuelve
    None.
    """
    try:
        product = Product.objects.get(id=id)
        if Product is not None:
            return product
    except (Product.DoesNotExist, Product.MultipleObjectsReturned) as err:
        print(err)
        return None
