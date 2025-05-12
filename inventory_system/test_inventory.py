from electronics import Electronics
from grocery import Grocery
from clothing import Clothing
from inventory import Inventory
from datetime import datetime

# Step 1: Create products
e1 = Electronics("E001", "Smartphone", 50000, 10, 2, "Samsung")
g1 = Grocery("G001", "Milk", 200, 20, "2025-06-01")
c1 = Clothing("C001", "Shirt", 1500, 5, "M", "Cotton")

# Step 2: Initialize inventory
inventory = Inventory()

# Step 3: Add products
inventory.add_product(e1)
inventory.add_product(g1)
inventory.add_product(c1)

# Step 4: List all products
print("\n--- All Products ---")
for p in inventory.list_all_products():
    print(p)

# Step 5: Sell a product
print("\n--- Selling 2 Shirts ---")
inventory.sell_product("C001", 2)
print(inventory._products["C001"])  # Check updated quantity

# Step 6: Restock a product
print("\n--- Restocking 5 Smartphones ---")
inventory.restock_product("E001", 5)
print(inventory._products["E001"])  # Check updated quantity

# Step 7: Search by name
print("\n--- Search for 'milk' ---")
results = inventory.search_by_name("milk")
for r in results:
    print(r)

# Step 8: Search by product type
print("\n--- Search by type: electronics ---")
results = inventory.search_by_type("electronics")
for r in results:
    print(r)

# Step 9: Total inventory value
print("\n--- Total Inventory Value ---")
print("Rs.", inventory.total_inventory_value())

# Step 10: Remove expired products
print("\n--- Testing Expired Removal ---")
expired = Grocery("G999", "Old Bread", 50, 3, "2023-01-01")
inventory.add_product(expired)
inventory.remove_expired_products()

print("\n--- Products After Removing Expired ---")
for p in inventory.list_all_products():
    print(p)

