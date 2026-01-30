class ConsoleUI:
    def __init__(self, service):
        self.service = service
    
    def run(self):
        while True: 
            print("1. Add Product")
            print("2. Modify Quantity")
            print("3. Filter Products by Name and Brand")
            print("4. Get Total Inventory Value")
            print("5. Exit")
            choice = input("Choose an option: ")

            if choice == "1":
                id = int(input("Enter product ID: "))
                name = input("Enter product name: ")
                brand = input("Enter product brand: ")
                quantity = int(input("Enter product quantity: "))
                price = float(input("Enter product price: "))
                self.service.add_product(id, name, brand, quantity, price)
                print("Product added successfully.")
            elif choice == "2":
                id = int(input("Enter product ID: "))
                new_quantity = int(input("Enter new quantity to deduct: "))
                try:
                    self.service.modify_the_quantity(id, new_quantity)
                    print("Quantity modified successfully.")
                except ValueError as ve:
                    print(f"Error: {ve}")
            elif choice == "3":
                string = input("Enter string to search in product names: ")
                brand = input("Enter brand to exclude: ")
                filtered_products = self.service.get_all_the_products_by_string_in_their_name(string, brand)
                for product in filtered_products:
                    print(product)
            elif choice == "4":
                total_value = self.service.get_total_inventory_value()
                print(f"Total Inventory Value: {total_value}")
            elif choice == "5":
                break