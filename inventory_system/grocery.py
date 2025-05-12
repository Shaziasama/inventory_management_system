
from product import Product
from datetime import datetime

class Grocery(Product):
    def __init__(self, product_id, name, price, quantity_in_stock, expiry_date):
        super().__init__(product_id, name, price, quantity_in_stock)
        self._expiry_date = datetime.strptime(expiry_date, "%Y-%m-%d").date()

    def is_expired(self):
        return datetime.now().date() > self._expiry_date

    def __str__(self):
        status = "Expired" if self.is_expired() else "Fresh"
        return (f"[Grocery] {self._name} - Rs.{self._price}, Stock: {self._quantity_in_stock}, "
                f"Expiry: {self._expiry_date} ({status})")
