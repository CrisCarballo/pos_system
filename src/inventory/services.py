from .models import Inventory


def update_inventory(product, quantity, transaction_type, notes):
    """
    La función actualiza el inventario de un producto determinado aumentando la cantidad si el producto
    ya existe en el inventario o creando una nueva entrada con la cantidad, el tipo de transacción y las
    notas especificadas.
    
    :param product: El parámetro del producto es el nombre o identificador del producto que se actualiza
    en el inventario
    :param quantity: El parámetro de cantidad representa la cantidad del producto que se actualiza en el
    inventario. Es un valor entero que indica el número de unidades del producto
    :param transaction_type: El parámetro "transaction_type" se utiliza para especificar el tipo de
    transacción que se realiza en el inventario. Podría ser una compra, venta, devolución, ajuste, etc.
    Esto ayuda a categorizar y rastrear los diferentes tipos de transacciones de inventario
    :param notes: El parámetro "notas" es una cadena que le permite agregar cualquier información
    adicional o comentarios relacionados con la actualización del inventario. Se puede utilizar para
    proporcionar detalles sobre la transacción, como el motivo de la actualización o instrucciones
    específicas
    """
    inventory_entry = Inventory.objects.filter(product=product).first()

    if inventory_entry:
        # Si el producto ya existe en el inventario, actualiza la cantidad
        inventory_entry.set_increase_quantity(quantity)
    else:
        # Si no crea una nueva entrada en el inventario para el producto
        Inventory.objects.create(
            product=product,
            quantity=quantity,
            transaction_type=transaction_type,
            notes=notes
        )