"""
Liskob substitution principle
"""


class Animal:
    def make_noise(self) -> None:
        raise NotImplementedError("You have to implement make_noise")

    def move(self) -> None:
        raise NotImplementedError("You have to implement move")


class Dog(Animal):
    def make_noise(self) -> None:
        print('Au Au')

    def move(self) -> None:
        print('Dog is moving...')


# Dog class entires substitute the animal class
# In other words, removing the class Animal and removing the extension
# Dog class 'll do the same job
dog = Dog()
dog.make_noise()
dog.move()
