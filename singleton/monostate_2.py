

class StringReprMixin:

    def __str__(self):

        params = ', '.join([f'{k}={v}' for k, v in self.__dict__.items()])
        return f'{self.__class__.__name__}({params})'

    def __repr__(self):
        return self.__str__()


class A(StringReprMixin):

    def __init__(self):

        self.x = 10
        self.y = 20


class MonoState(StringReprMixin):
    _state: dict = {}

    def __new__(cls, *args, **kwargs):

        obj = super().__new__(cls)
        obj.__dict__ = cls._state

        return obj

    def __init__(self, nome=None, sobrenome=None):

        self.__dict__ = self._state

        if nome is not None:
            self.nome = nome

        if sobrenome is not None:
            self.sobrenome = sobrenome


if __name__ == "__main__":

    m1 = MonoState('Paulo')
    print(m1)

    m2 = MonoState()
    print(m2)
