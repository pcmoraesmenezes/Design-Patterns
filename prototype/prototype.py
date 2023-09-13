"""
Especificar os tipos de objetos a serem criados usando uma instância protótipo
e criar novos objetos pela cópia desse protótipo.

O padrão Prototype permite que você produza diferentes tipos e representações
de um objeto usando o mesmo código de construção.

O padrão Prototype resolve o problema anti-padrão telescoping constructor,
que ocorre quando o aumento do número de parâmetros de um construtor torna
impossível escrever sobrecargas para todos eles. O padrão Prototype permite
que você construa objetos passo a passo, usando apenas aqueles construtores
que você realmente precisa.
"""
from __future__ import annotations
from typing import List


class StringReprMixin:

    def __str__(self):

        params = ', '.join([f'{k}={v}' for k, v in self.__dict__.items()])
        return f'{self.__class__.__name__}({params})'

    def __repr__(self):
        return self.__str__()


class Person(StringReprMixin):

    def __init__(self, firstname: str, lastname: str) -> None:

        self.firstname = firstname
        self.lastname = lastname
        self.address: List[Address] = []

    def add_address(self, address: Address) -> None:
        self.address.append(address)

    def clone(self) -> Person:
        return deepcopy(self)


class Address(StringReprMixin):

    def __init__(self, street: str, number: str) -> None:

        self.street = street
        self.number = number


if __name__ == "__main__":

    from copy import deepcopy

    paulo = Person('Paulo', 'César')
    endereco_paulo = Address('Rua das Flores', '123')
    paulo.add_address(endereco_paulo)
    print(paulo)

    print()

    esposa_paulo = paulo.clone()
    esposa_paulo.firstname = 'Maria'
    esposa_paulo.lastname = 'Silva'
    print(esposa_paulo)
