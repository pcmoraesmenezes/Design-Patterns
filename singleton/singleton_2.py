def singleton(the_class):
    instances = {}

    def get_class(*args, **kwargs):
        if the_class not in instances:
            instances[the_class] = the_class(*args, **kwargs)

        return instances[the_class]

    return get_class


@singleton
class AppSettings:
    def __init__(self):
        print('OI')  # Note que o método __init__ é chamado apenas uma vez
        self.tema = "O tema escuro"


@singleton
class Teste:
    def __init__(self):
        print('OI DENOVO')


if __name__ == "__main__":
    as1 = AppSettings()
    as1.tema = "O tema claro"
    print(as1.tema)  # O tema claro

    as2 = AppSettings()
    print(as1.tema)  # O tema é sobrescrito toda vez que um objeto é instanciado  # noqa
    print(as1 == as2)  # eles são os mesmo objetos na memória

    t1 = Teste()
    t2 = Teste()
    print(t1 == t2)
