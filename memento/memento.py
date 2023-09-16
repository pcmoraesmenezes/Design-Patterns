"""
GOF - Memento é um padrão de projeto comportamental que tem a
intenção de permitir que você salve e restaure o estado anterior
de um objeto sem revelar os detalhes de sua implementação.

- O Memento permite que você faça snapshots do estado de um objeto
e salve-o externamente para que possa restaurar o objeto para esse
estado mais tarde.

- O Memento mantém o estado do Memento imutável, de modo que apenas
o objeto que criou pode acessá-lo.
"""
from __future__ import annotations
from typing import Dict, List
from copy import deepcopy


class Memento:

    def __init__(self, state: Dict) -> None:

        self._state: Dict
        super().__setattr__('_state', state)

    def get_state(self) -> Dict:

        return self._state

    def __setattr__(self, name, value):
        raise AttributeError("Can't set attribute")


class ImageEditor:

    def __init__(self, name: str, width: int, height: int) -> None:

        self.name = name
        self.width = width
        self.height = height

    def save_state(self) -> Memento:

        return Memento(deepcopy(self.__dict__))

    def restore(self, memento: Memento) -> None:

        self.__dict__ = memento.get_state()

    def __str__(self) -> str:

        return f"{self.__class__.__name__} ({self.__dict__})\n"


class Caretaker:

    def __init__(self, originator: ImageEditor) -> None:

        self._originator = originator
        self._mementos: List[Memento] = []

    def backup(self) -> None:

        self._mementos.append(self._originator.save_state())

    def restore(self) -> None:

        if not self._mementos:
            return

        self._originator.restore(self._mementos.pop())


if __name__ == "__main__":

    img = ImageEditor('FOTO_1.jpg', 200, 200)
    print(img)

    caretaker = Caretaker(img)

    caretaker.backup()

    img.name = 'FOTO_2.jpg'
    img.width = 400
    img.height = 400

    print(img)

    caretaker.restore()

    print(img)
