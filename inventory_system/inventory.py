class Inventory:
    def __init__(self):
        self._products = {}

    def add_product(self, product):
        if product._product_id in self._products:
            raise ValueError("Product with this ID already exists.")
        self._products[product._product_id] = product

    def remove_product(self, product_id):
        if product_id in self._products:
            del self._products[product_id]

    def search_by_name(self, name):
        return [p for p in self._products.values() if name.lower() in p._name.lower()]

    def search_by_type(self, product_type):
        return [p for p in self._products.values() if p.__class__.__name__.lower() == product_type.lower()]

    def list_all_products(self):
        return list(self._products.values())

    def sell_product(self, product_id, quantity):
        if product_id in self._products:
            self._products[product_id].sell(quantity)

    def restock_product(self, product_id, quantity):
        if product_id in self._products:
            self._products[product_id].restock(quantity)

    def total_inventory_value(self):
        return sum(p.get_total_value() for p in self._products.values())

    def remove_expired_products(self):
        expired = [pid for pid, p in self._products.items()
                   if p.__class__.__name__ == "Grocery" and p.is_expired()]
        for pid in expired:
            del self._products[pid]
