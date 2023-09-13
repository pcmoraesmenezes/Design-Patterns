"""
Strategy é um padrão de projeto comportamental que tem a intenção
de definir uma família de algoritmos, encapsular cada uma delas e
torná-las intercambiáveis. Strategy permite que o algoritmo varie
independentemente dos clientes que o utilizam.

O padrão Strategy permite que você altere o objeto que executa um
determinado comportamento em tempo de execução.

Principio:
    "Programar para uma interface, não para uma implementação."

O padrão Strategy é muito parecido com o padrão State. Ambos podem
ser baseados na mesma estrutura de classes. A diferença chave é que,
no padrão State, os objetos de contexto podem mudar sua classe de
estado a qualquer momento, enquanto que, com Strategy, a estratégia
completa do objeto precisa ser substituída de uma vez. No entanto,
as duas implementações são baseadas na injeção de dependência:
os objetos de contexto (ou clientes) recebem uma estratégia
concreta do objeto criador, ao invés de criá-la por conta própria.

"""
from __future__ import annotations
from abc import ABC, abstractmethod


class Order:

    def __init__(self, total: float, discount: DiscountStrategy):

        self._total = total
        self._discount = discount

    @property
    def total(self):
        return self._total

    @property
    def total_with_discount(self):
        return self._discount.calculate(self.total)

    def __repr__(self):
        return f'Total: {self.total}, Total com desconto: ' \
               f'{self.total_with_discount}\n'


class DiscountStrategy(ABC):

    @abstractmethod
    def calculate(self, value: float) -> float:
        pass


class TwentyPercent(DiscountStrategy):

    def calculate(self, value: float) -> float:
        return value - (value * 0.2)


class NoDiscount(DiscountStrategy):

    def calculate(self, value: float) -> float:
        return value


class FiftyPercent(DiscountStrategy):

    def calculate(self, value: float) -> float:
        return value - (value * 0.5)


class CustomDiscount(DiscountStrategy):

    def __init__(self, discount: float) -> None:

        try:
            self._discount = discount / 100
            assert self._discount < 1, ('O desconto precisa ser um valor < 100')  # noqa

        except TypeError:
            assert ('O desconto precisa ser um valor em porcentagem')

    def calculate(self, value: float) -> float:
        return value - (value * self._discount)


if __name__ == "__main__":
    order = Order(1000, TwentyPercent())
    print(order)

    order2 = Order(1000, FiftyPercent())
    print(order2)

    order3 = Order(1000, NoDiscount())
    print(order3)

    order4 = Order(1000, CustomDiscount(10))
    print(order4)

    order5 = Order(1000, CustomDiscount(101))
    print(order5)

    # order6 = Order(1000, CustomDiscount('10'))
    # print(order6)
