# main.py

from inventory_utils import restock_product

# Base Product Class
class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def total_value(self):
        return self.price * self.quantity

    def __str__(self):
        return f"{self.name} | Price: ${self.price:.2f} | Qty: {self.quantity}"

# Subclass for Perishable Products
class PerishableProduct(Product):
    def __init__(self, name, price, quantity, expiry_days):
        super().__init__(name, price, quantity)
        self.expiry_days = expiry_days

    def total_value(self):
        total = super().total_value()
        if self.expiry_days < 5:
            total *= 0.8  # 20% discount
        return total

    def __str__(self):
        return f"{super().__str__()} | Expiry in {self.expiry_days} days"

# Inventory Manager Class
class InventoryManager:
    def __init__(self):
        self.inventory = []

    def add_product(self, product):
        self.inventory.append(product)

    def list_inventory(self):
        print("\n Inventory List:")
        for i, item in enumerate(self.inventory, 1):
            print(f"{i}. {item} | Total Value: ${item.total_value():.2f}")

    def search_by_name(self, term):
        print(f"\n Search Results for '{term}':")
        results = list(filter(lambda p: term.lower() in p.name.lower(), self.inventory))
        for item in results:
            print(f"- {item}")

    def restock_all(self):
        for product in self.inventory:
            restock_product(product)

    def export_summary(self, filename="inventory_report.txt"):
        with open(filename, "w") as f:
            f.write(" Inventory Summary Report\n")
            f.write("-" * 30 + "\n")
            summary = {
                product.name: {
                    "price": product.price,
                    "quantity": product.quantity,
                    "total_value": product.total_value()
                }
                for product in self.inventory
            }
            for name, details in summary.items():
                f.write(
                    f"{name}: Price=${details['price']:.2f}, Qty={details['quantity']}, "
                    f"Total=${details['total_value']:.2f}\n"
                )
        print("\n Summary exported to inventory_report.txt")

# === Main Execution ===
if __name__ == "__main__":
    manager = InventoryManager()

    # Add products
    manager.add_product(Product("Laptop", 800, 5))
    manager.add_product(Product("Mouse", 20, 15))
    manager.add_product(PerishableProduct("Milk", 2.5, 10, 3))  # should get 20% discount
    manager.add_product(PerishableProduct("Bread", 1.5, 20, 7))

    manager.list_inventory()
    manager.search_by_name("milk")

    manager.restock_all()
    print("\n After Restocking:")
    manager.list_inventory()

    manager.export_summary()
