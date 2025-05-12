from product import Product

class Clothing(Product):
    def __init__(self, product_id, name, price, quantity_in_stock, size, material):
        super().__init__(product_id, name, price, quantity_in_stock)
        self._size = size
        self._material = material

    def __str__(self):
        return (f"[Clothing] {self._name} - Rs.{self._price}, Stock: {self._quantity_in_stock}, "
                f"Size: {self._size}, Material: {self._material}")
