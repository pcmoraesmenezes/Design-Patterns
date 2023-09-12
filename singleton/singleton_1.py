"""
A intenção do Singleton é de garantir que uma classe
tenha apenas uma instância e que forneça um ponto global
de acesso a ela.

Caso se instancie uma classe Singleton, o objeto retornado
será sempre o mesmo.

O Singleton é um padrão de projeto criacional que permite
garantir que uma classe tenha apenas uma instância, enquanto
fornece um ponto de acesso global a essa instância.

O Singleton resolve problemas como:

- Garantir que uma classe tenha apenas uma instância;
- Fornecer um ponto de acesso global a essa instância.

O Singleton tem quase os mesmos prós e contras que variáveis
globais. Embora sejam muito úteis, eles violam o princípioN
de responsabilidade única da SOLID.

O padrão tem apenas um ponto negativo significativo - ele
torna o código do programa mais difícil de testar, pois
introduz estado global no código. É possível contornar esse
problema, mas para isso, o código do programa precisa ser
modificado para que as classes Singleton recebam o objeto
que devem usar como parâmetro em vez de criá-lo por conta
própria.
"""


class AppSettings:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)

        return cls._instance

    def __init__(self):
        self.tema = "O tema escuro"


if __name__ == "__main__":
    as1 = AppSettings()
    as1.tema = "O tema claro"
    print(as1.tema)  # O tema claro

    as2 = AppSettings()
    print(as1.tema)  # O tema é sobrescrito toda vez que um objeto é instanciado  # noqa
    print(as1 == as2)  # eles são os mesmo objetos na memória
