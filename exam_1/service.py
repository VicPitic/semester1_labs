from domain import Product

class ProductService:
    def __init__(self, repository):
        self._repository = repository

    def add_product(self, id, name, brand, quantity, price):
        product = Product(id, name, brand, quantity, price)
        self._repository.add_product(product)

    def validate_quantity (self, id, quantity):
        if quantity < 0:
            raise ValueError("Quantity cannot be negative")
        products = self._repository.get_all_products()
        for product in products:
            if product.id == id and quantity > product.quantity:
                raise ValueError("Insufficient quantity available")
            
    def validate_product_id(self, id): 
        products = self._repository.get_all_products()
        for product in products:
            if product.id == id:
                return
        raise ValueError("Product ID does not exist")

    def modify_the_quantity(self, id, new_quantity):
        
        self.validate_product_id(id)
        self.validate_quantity(id, new_quantity)
        
        products = self._repository.get_all_products()
        for product in products:
            if product.id == id:
                product.quantity -= new_quantity
        self._repository._save()

    def get_all_the_products_by_string_in_their_name(self, string, brand):
        products = self._repository.get_all_products()
        filtered_products = []
        for product in products:
            if string in product.name and product.brand != brand:
                filtered_products.append(product)
        return filtered_products
    
    def get_total_inventory_value(self):
        products = self._repository.get_all_products()
        total_value = 0
        for product in products:
            total_value += product.quantity * product.price
        return total_value