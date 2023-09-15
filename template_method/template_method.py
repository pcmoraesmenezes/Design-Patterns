"""
Template Method (Comportamental) tem a intenção de definir
um algoritmo em um método, postergando alguns passos
para as subclasses por herança. Template Method permite
que subclasses redefinam certos passos de um algoritmo
sem mudar a estrutura do mesmo.

O Template Method sugere que você divida o algoritmo em
uma série de etapas, converta essas etapas em métodos e
coloque uma série de chamadas de suas subclasses. Você
pode fazer com que suas subclasses implementem esses
métodos se quiser ou simplesmente fornecer a elas os
métodos padrão.
"""
from abc import ABC, abstractmethod


class Abstract(ABC):
    def template_method(self):
        self.operation1()
        self.hook1()
        self.operation2()

    def hook1(self):
        pass

    @abstractmethod
    def operation1(self):
        ...

    @abstractmethod
    def operation2(self):
        ...


class Concrete(Abstract):

    def hook1(self):
        print("Concrete hook 1 overriden")

    def operation1(self):
        print("Concrete operation 1")

    def operation2(self):
        print("Concrete operation 2")


class Concrete2(Abstract):
    def operation1(self):
        print("Concrete operation of New class")

    def operation2(self):
        print("Concrete operation of New Class")


if __name__ == "__main__":
    c = Concrete()
    c.template_method()
    # Note o principio da Inversão de Controle, onde a classe
    # mãe chama os métodos das classes filhas.
    c2 = Concrete2()
    c2.template_method()
