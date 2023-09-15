"""
Iterator é um padrão comportamental que tem a intenção de fornecer
um meio de acessar, sequencialmente, os elementos de um objeto agre
gado sem expor sua representação subjacente.

- Uma coleção deve fornecer um meio de acessar
        seus elementos sem expor sua estrutura interna.

- Uma coleção deve fornecer meios de percorrer seus elementos
        sem expor sua estrutura interna.

- Uma coleção deve ser capaz de fornecer mais de um iterador.

- O acesso aos elementos de uma coleção deve ser independentes
        de como ela é implementada.

A ideia principal do padrão Iterator é retirar a responsabilidade
de acesso e percurso dos elementos de uma coleção e delegar para
um objeto iterador.
"""

from collections.abc import Iterator, Iterable
from typing import Any, List


class MyIterator(Iterator):

    def __init__(self, collection: List[Any]) -> None:
        self._collection = collection
        self._index = 0

    def next(self):
        try:
            return self.__next__()
        except StopIteration:
            raise StopIteration

    def __next__(self):

        try:

            item = self._collection[self._index]
            self._index += 1
            return item

        except IndexError:
            raise StopIteration


class ReverseIterator(Iterator):

    def __init__(self, collection: List[Any]) -> None:
        self._collection = collection
        self._index = -1

    def next(self):
        try:
            return self.__next__()
        except StopIteration:
            raise StopIteration

    def __next__(self):

        try:

            item = self._collection[self._index]
            self._index -= 1
            return item

        except IndexError:
            raise StopIteration


class MyList(Iterable):

    def __init__(self) -> None:
        self._items: List[Any] = []
        self._my_iterator = MyIterator(self._items)

    def add(self, value: Any) -> None:
        self._items.append(value)

    def __iter__(self) -> MyIterator:
        return MyIterator(self._items)

    def reverse_iterator(self) -> ReverseIterator:
        return ReverseIterator(self._items)

    def __str__(self) -> str:
        return f"{self.__class__.__name__}({self._items})"


if __name__ == "__main__":

    mylist = MyList()
    mylist.add('Paulo')
    mylist.add('Tereza')
    mylist.add('A vestruz')

    for value in mylist:
        print(value)

    print()

    for value in mylist.reverse_iterator():
        print(value)
