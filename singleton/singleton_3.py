# class Meta(type):
#     def __call__(cls, *args, **kwargs):
#         print('CALL DA METACLASS')
#         return super().__call__(*args, **kwargs)


# class Pessoa(metaclass=Meta):

#     def __new__(cls, *args, **kwargs):
#         print('New é executado')
#         return super().__new__(cls)

#     def __init__(self, nome):
#         print('Init é executado')
#         self.nome = nome

#     def __call__(self, x, y):
#         print('Chamando o método call ', self.nome, x + y)


# p1 = Pessoa('Fabio')
# p1(1, 2)  # Chamando o método call


class Singleton(type):

    _instaces: dict = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instaces:
            cls._instaces[cls] = super().__call__(*args, **kwargs)

        return cls._instaces[cls]


class AppSettings(metaclass=Singleton):

    def __init__(self):
        self.tema = "O tema escuro"


if __name__ == "__main__":
    as1 = AppSettings()
    as1.tema = "O tema claro"
    print(as1.tema)  # O tema claro

    as2 = AppSettings()
    print(as1.tema)  # O tema é sobrescrito toda vez que um objeto é instanciado  # noqa
    print(as1 == as2)  # eles são os mesmo objetos na memória
