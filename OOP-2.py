class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Cart:
    def __init__(self):
        self.items = []

    def add_product(self, product):
        self.items.append(product)
        print(product.name, "added to cart")

    def show_cart(self):
        if not self.items:
            print("Cart is empty")
            return

        total = 0
        print("\nItems in Cart:")

        for item in self.items:
            print(item.name, "-", item.price)
            total += item.price

        print("Total Price:", total)


# Product List
p1 = Product("Laptop", 50000)
p2 = Product("Phone", 20000)
p3 = Product("Headphones", 2000)

products = [p1, p2, p3]

cart = Cart()

while True:

    print("\n1 Show Products")
    print("2 Add to Cart")
    print("3 View Cart")
    print("4 Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        print("\nAvailable Products")
        for i, p in enumerate(products, 1):
            print(i, p.name, "-", p.price)

    elif choice == "2":
        num = int(input("Enter product number: "))
        if 1 <= num <= len(products):
            cart.add_product(products[num-1])
        else:
            print("Invalid product")

    elif choice == "3":
        cart.show_cart()

    elif choice == "4":
        print("Thank you for shopping")
        break

    else:
        print("Invalid choice")
