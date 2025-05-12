from product import Product

class Electronics(Product):
    def __init__(self, product_id, name, price, quantity_in_stock, warranty_years, brand):
        super().__init__(product_id, name, price, quantity_in_stock)
        self._warranty_years = warranty_years
        self._brand = brand

    def __str__(self):
        return (f"[Electronics] {self._name} ({self._brand}) - Rs.{self._price}, "
                f"Stock: {self._quantity_in_stock}, Warranty: {self._warranty_years} years")

