"""
Mediator é um padrão de projeto comportamental que tem a intenção
de definir um objeto que encapsula a forma como um conjunto de
objetos interage. O Mediator promove o baixo acoplamento ao evitar
que os objetos se refiram uns aos outros explicitamente e permite
variar suas interações independentemente.
"""
from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List


class Colleague(ABC):

    def __init__(self) -> None:

        self.name: str

    @abstractmethod
    def broadcast(self, message: str) -> None:
        pass

    @abstractmethod
    def direct(self, msg: str) -> None:
        pass


class Person(Colleague):

    def __init__(self, name: str, mediator: Mediator) -> None:

        self.name = name
        self.mediator = mediator

    def broadcast(self, message: str) -> None:
        ...

    def direct(self, msg: str) -> None:
        print(msg)


class Mediator(ABC):

    @abstractmethod
    def broadcast(self, person: Colleague, msg: str) -> None:
        pass

    @abstractmethod
    def direct(self, sender: Colleague, receiver: str, msg: str) -> None:
        pass


class ChatRoom(Mediator):

    def __init__(self) -> None:

        self.colleagues: List[Colleague] = []

    def is_colleague(self, colleague: Colleague) -> bool:

        return colleague in self.colleagues

    def add(self, colleague: Colleague) -> None:

        if not self.is_colleague(colleague):
            self.colleagues.append(colleague)

    def remove(self, colleague: Colleague) -> None:

        if self.is_colleague(colleague):
            self.colleagues.remove(colleague)

    def broadcast(self, colleague: Colleague, msg: str) -> None:

        if not self.is_colleague(colleague):
            return

        print(f'{colleague.name} says: {msg}')

    def direct(self, sender: Colleague, receiver: str, msg: str) -> None:

        if not self.is_colleague(sender):
            return

        receiver_object: List[Colleague] = [
            colleague for colleague in self.colleagues
            if colleague.name == receiver
        ]

        if not receiver_object:
            return

        receiver_object[0].direct(
            f'{sender.name} says to {receiver}: {msg}'
        )


if __name__ == "__main__":

    chat_room = ChatRoom()

    john = Person('John', chat_room)
    jane = Person('Jane', chat_room)
    alice = Person('Alice', chat_room)

    chat_room.add(john)
    chat_room.add(jane)
    chat_room.add(alice)

    john.direct('Hello everyone!')
    jane.direct('Hi John!')

    chat_room.direct(john, 'Jane', 'Hi Jane!')
    chat_room.direct(jane, 'Alice', 'Hello Alice!')
    chat_room.direct(alice, 'John', 'Hi John!')

    chat_room.broadcast(john, 'Hello everyone!')
    chat_room.broadcast(jane, 'Hi John!')
    chat_room.broadcast(alice, 'Hi John!')
