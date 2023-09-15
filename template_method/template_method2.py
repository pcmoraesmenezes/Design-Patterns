from abc import ABC, abstractmethod


class Pizza(ABC):
    def prepare(self):
        self.add_ingridients()
        self.cook()
        self.cut()
        self.serve()
        self.done()

    def cut(self):
        print(f"Cutting pizza: {self.__class__.__name__}\n")

    def serve(self):
        print(f"Serving pizza: {self.__class__.__name__}\n")

    def done(self):
        print(f"Done pizza: {self.__class__.__name__}\n")

    @abstractmethod
    def add_ingridients(self):
        pass

    @abstractmethod
    def cook(self):
        pass


class CatupiryPizza(Pizza):
    def add_ingridients(self):
        print("Adding catupiry\n")

    def cook(self):
        print("Cooking for 10 minutes\n")


class FourCheesePizza(Pizza):
    def add_ingridients(self):
        print("Adding 4 cheeses\n")

    def cook(self):
        print("Cooking for 20 minutes\n")


if __name__ == "__main__":
    catupiry_pizza = CatupiryPizza()
    catupiry_pizza.prepare()

    four_cheese_pizza = FourCheesePizza()
    four_cheese_pizza.prepare()
