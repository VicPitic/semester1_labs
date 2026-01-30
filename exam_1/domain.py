class Product:
    def __init__(self, id, name, brand, quantity, price):
        self.id = id
        self.name = name
        self.brand = brand
        self.quantity = quantity
        self.price = price

    def __str__(self):
        return f"ID: {self.id}, Name: {self.name}, Brand: {self.brand}, Quantity: {self.quantity}, Price: {self.price}"
    