from .product import Product

class Inventory:
    def __init__(self):
        self._products = []
    
    def add_product(self, product: Product) -> None:
        for existing_product in self._products:
            if existing_product == product:
                existing_product.quantity += product.quantity
                return
        self._products.append(product)
    
    def remove_product(self, product_name: str) -> None:
        product = self.get_product(product_name)
        if product:
            self._products.remove(product)
        else:
            raise ValueError(f"Product '{product_name}' not found in inventory")
    
    def get_product(self, product_name: str) -> Product | None:
        for product in self._products:
            if product.name == product_name:
                return product
        return None
    
    def total_inventory_value(self) -> float:
        return sum(product.get_value() for product in self._products)