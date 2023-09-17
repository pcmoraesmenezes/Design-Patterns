"""
O proxy é um padrão de projeto estrutural que tem a intenção de
fornecer um objeto substituto que atua como se fosse o objeto real.

Um proxy recebe as solicitações do cliente e as repassa ao objeto
real, mantendo uma referência a ele. O objeto proxy pode ser
responsável por sua criação e destruição. O proxy também pode
controlar o acesso ao objeto real, permitindo ou não que o cliente
faça solicitações adicionais.

O proxy é um padrão de projeto muito popular em aplicações escritas
em Java. A implementação do padrão depende muito do uso de recursos
de reflexão da linguagem. Em Python, a implementação do padrão é
mais simples pois a linguagem já possui um suporte nativo ao
paradigma de programação orientada a objetos.
"""
from __future__ import annotations
from abc import ABC, abstractmethod
from time import sleep
from typing import List, Dict


class IUser(ABC):
    firstname: str
    lastname: str

    @abstractmethod
    def get_addresses(self) -> List[Dict]:
        pass

    @abstractmethod
    def get_all_user_data(self) -> Dict:
        pass


class User(IUser):

    def __init__(self, firstname: str, lastname: str) -> None:
        sleep(2)
        self.firstname = firstname
        self.lastname = lastname

    def get_addresses(self) -> List[Dict]:
        sleep(3)
        return [
            {'street': 'Av. Brasil', 'number': 1000},
            {'street': 'Av. Paulista', 'number': 2000},
        ]

    def get_all_user_data(self) -> Dict:
        sleep(3)
        return {
            'firstname': self.firstname,
            'lastname': self.lastname,
            'addresses': self.get_addresses()
        }


class UserProxy(IUser):

    def __init__(self, firstname: str, lastname: str) -> None:
        self.firstname = firstname
        self.lastname = lastname
        self.user: User
        self._cached_addresses: List[Dict] = []
        self._all_user_data: Dict = {}

    def get_addresses(self) -> List[Dict]:

        self.get_user()
        if not hasattr(self, '_cached_addresses'):

            self._cached_addresses = self.user.get_addresses()

        return self._cached_addresses

    def get_all_user_data(self) -> Dict:

        self.get_user()
        if not hasattr(self, '_all_user_data'):
            self._all_user_data = self.user.get_all_user_data()

        return self._all_user_data

    def get_user(self) -> None:

        if not hasattr(self, 'user'):
            self.user = User(self.firstname, self.lastname)


if __name__ == "__main__":

    user = UserProxy('John', 'Doe')
    print(user.firstname)
    print(user.lastname)

    print(user.get_all_user_data())
    print(user.get_addresses())
