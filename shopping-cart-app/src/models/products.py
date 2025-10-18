from abc import ABC, abstractmethod

class Product(ABC):
    def __init__(self, name, price):
        self._name = name
        self._price = price

    @property
    def name(self):
        return self._name

    @property
    def price(self):
        return self._price

    @abstractmethod
    def get_details(self):
        pass

class Electronics(Product):
    def __init__(self, name, price):
        super().__init__(name, price)
        print("Constructor for Electronics")

    def get_details(self):
        return f"The name is {self._name} and price is ${self._price}"

class Clothing(Product):
    def __init__(self, name, price):
        super().__init__(name, price)
        print("Constructor for Clothing")

    def get_details(self):
        return f"The name is {self._name} and price is ${self._price}"

class Grocery(Product):
    def __init__(self, name, price):
        super().__init__(name, price)
        print("Constructor for Grocery")

    def get_details(self):
        return f"The name is {self._name} and price is ${self._price}"