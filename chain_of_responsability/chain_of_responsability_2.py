from abc import ABC, abstractmethod


class Handler(ABC):

    def __init__(self) -> None:
        self.sucessor: Handler

    @abstractmethod
    def handle(self, letter: str) -> str:
        pass


class Handler_ABC(Handler):

    def __init__(self, sucessor: Handler) -> None:
        self.sucessor = sucessor
        self.letters = ['A', 'B', 'C']

    def handle(self, letter: str) -> str:
        if letter in self.letters:
            return f'Handler_ABC: conseguiu tratar {letter}\n'
        return self.sucessor.handle(letter)


class Handler_DEF(Handler):

    def __init__(self, sucessor: Handler) -> None:
        self.sucessor = sucessor
        self.letters = ['D', 'E', 'F']

    def handle(self, letter: str) -> str:
        if letter in self.letters:
            return f'Handler_DEF: conseguiu tratar {letter}\n'
        return self.sucessor.handle(letter)


class Handler_unsolved(Handler):

    def handle(self, letter: str) -> str:
        return f'Handler_unsolved: não conseguiu tratar {letter}\n'


if __name__ == "__main__":
    handler_ABC = Handler_ABC(Handler_DEF(Handler_unsolved()))
    print(handler_ABC.handle('A'))
    print(handler_ABC.handle('B'))
    print(handler_ABC.handle('C'))
    print(handler_ABC.handle('D'))
    print(handler_ABC.handle('E'))
    print(handler_ABC.handle('F'))
    print(handler_ABC.handle('G'))
    print(handler_ABC.handle('H'))
    print(handler_ABC.handle('I'))
    print(handler_ABC.handle('J'))
    print(handler_ABC.handle('K'))
    print(handler_ABC.handle('L'))
    print(handler_ABC.handle('M'))
    print(handler_ABC.handle('N'))
    print(handler_ABC.handle('O'))
    print(handler_ABC.handle('P'))
    print(handler_ABC.handle('Q'))
    print(handler_ABC.handle('R'))
    print(handler_ABC.handle('S'))
    print(handler_ABC.handle('T'))
    print(handler_ABC.handle('U'))
    print(handler_ABC.handle('V'))
    print(handler_ABC.handle('W'))
    print(handler_ABC.handle('X'))
    print(handler_ABC.handle('Y'))
    print(handler_ABC.handle('Z'))
