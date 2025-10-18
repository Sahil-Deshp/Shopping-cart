from exceptions.custom_exceptions import OutOfStock
from models.products import Electronics, Clothing, Grocery

class ShoppingCart:
    def __init__(self):
        self.items = []
        self.total = 0
        print("Welcome to Cart --- :")

    def add_item(self, category, name, price):
        if category == "e":
            item = Electronics(name, price)
        elif category == "c":
            item = Clothing(name, price)
        elif category == "g":
            item = Grocery(name, price)
        else:
            raise OutOfStock("Invalid category")
            
        self.items.append(item)
        self.total += price
        item.get_details()

    def get_total(self):
        return self.total

    def show_cart(self):
        if not self.items:
            print("Cart is empty!")
            return
            
        print("\nCart Contents:")
        for item in self.items:
            print(item.get_details())
        print(f"Total Price: ${self.total:.2f}")