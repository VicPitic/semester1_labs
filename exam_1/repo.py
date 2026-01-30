from domain import Product

class ProductRepository:
    def __init__(self, filename):
        self._filename = filename
        self._products = []
        self._load()

    def _load(self):
        self._products = [] 

        with open(self._filename, "r") as file:
            for line in file: 
                id, name, brand, quantity, price = line.strip().split(",")
                product = Product(int(id), name, brand, int(quantity), float(price))
                self._products.append(product)

    def _save(self):
        with open(self._filename, "w") as file:
            for product in self._products:
                file.write(f"{product.id},{product.name},{product.brand},{product.quantity},{product.price}\n")         

    def add_product(self, product):
        self._load()
        self._products.append(product)
        self._save()   
    
    def get_all_products(self):
        self._load()
        return self._products