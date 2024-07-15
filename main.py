# Defining product class with their states
class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity


# Defining Shopping Cart class
class ShoppingCart:
    def __init__(self):
        self.items = []

    # Defining Add Item method
    def add_item(self, product, quantity):
        self.items.append({"product": product, "quantity": quantity})


# Defining Epharmacy class
class EPharmacy:
    def __init__(self):
        self.products = []


    # Defining Add Product method
    def add_product(self, name, price, quantity):
        self.products.append(Product(name, price, quantity))


    # Defining method to display products
    def display_products(self):
        for i, product in enumerate(self.products, 1):
            print(f"{i}. {product.name}: ${product.price} ({product.quantity} available)")


    # Defining method to process order
    def process_order(self, shopping_cart):
        total_cost = 0

        for item in shopping_cart.items:
            total_cost += item["product"].price * item["quantity"]
            item["product"].quantity -= item["quantity"]
            print("Order processed succefully!")
            print(f"Total cost: ${total_cost: .2f}")


pharmacy = EPharmacy()

# Creating Console based User interface
while True:

    print("\nWelcome to E-Pharmacy!")
    print("1. Add product")
    print("2. Display products")
    print("3. Process order")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":

        name = input("Enter product name: ")
        price = float(input("Enter product price: "))
        quantiy = int(input("Enter product quantity: "))
        pharmacy.add_product(name, price, quantity)

    elif choice == "2":

        pharmacy.display_products()

    elif choice == "3":

        cart = ShoppingCart()
        pharmacy.display_products()

        while True:

            product_choice = input("Enter the product number to add to cart (0 'done' to finish): ")

            if product_choice.lower() == "done":
                break
            try:
                product_index = int(product_choice) - 1

                if 0 <= product_index < len(pharmacy.products):
                    quantiy = int(input("Enter quantity:"))

                    if pharmacy.products[product_index].quantity >= quantity:
                        cart.add_item(pharmacy.products[product_index], quantiy)

                    else:
                        print("Insufficient stock!")

                else:
                    print("Invalid product number!")

            except ValueError:
                print("Invalid input. please enter a product number or 'done' to finish.")
        pharmacy.process_order(cart)

    elif choice == "4":
        print("Thank you for shopping at E-Pharmacy!")
        break

    else:
        print("Invalid choice! Please enter a number from 1 - 4.")
