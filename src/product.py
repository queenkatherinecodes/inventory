class Product:
    def __init__(self, name: str, price: float, quantity: int):
        self.name = name
        self.price = price
        self.quantity = quantity
    
    def get_value(self) -> float:
        return self.price * self.quantity
    
    def __eq__(self, other):
        if not isinstance(other, Product):
            return False
        return self.name == other.name