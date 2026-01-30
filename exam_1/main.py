from repo import ProductRepository
from service import ProductService
from ui import ConsoleUI

repo = ProductRepository("products.txt")
service = ProductService(repo)
ui = ConsoleUI(service)

if __name__ == "__main__":
    ui.run()
