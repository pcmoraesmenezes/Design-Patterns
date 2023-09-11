"""
Factory method é um padrão de criação que permite definir uma interface
para criar objetos, mas deixa as subclasses decidirem quais objetos criar.

Factory method permite adiar a instanciação para subclasses.

Podem facilitar o processo de "cache" ou criação de "singletons" porque


Em POO, o termo factory refere-se a uma classe ou metodo que é respnsavel por
criar objetos.

Vantagens:
    Permitem criar um sistema com baixo acoplamento entre classes porque
    ocultam as classes que criam os objetos do código cliente.

    Permitem a fácil substituição de objetos de um mesmo tipo.

    Permitem a fácil adição de novos objetos ao sistema, sem que haja a

    Podem facilitar o processo de "cache" ou criação de "singletons" porque
    a fabrica pode retornar um objeto já criado para o cleinte, ao invés de
    criar novos objetos sempre que o cliente precisar.

Desvantagens:
    Podem introduzir muitas classes no sistema, aumentando a complexidade do
    código.

    Podem introduzir um novo ponto de falha. Se a fabrica falhar, todo o
    sistema falha.

    Podem ser desnecessárias se o sistema não precisar criar muitos objetos
"""
from abc import ABC, abstractmethod
from random import choice


class Veiculo(ABC):
    @abstractmethod
    def buscar_cliente(self) -> None:
        pass


class CarroLuxo(Veiculo):
    def buscar_cliente(self) -> None:
        print("Carro de luxo está buscando o cliente...")


class CarroPopular(Veiculo):
    def buscar_cliente(self) -> None:
        print("Carro popular está buscando o cliente...")


class Moto(Veiculo):
    def buscar_cliente(self) -> None:
        print("Moto está buscando o cliente...")

# Fabrica


class VeiculoFactory:
    def __init__(self, tipo):
        self.carro = self.get_carro(tipo)

    @staticmethod
    @abstractmethod
    def get_carro(tipo: str) -> Veiculo:  # type: ignore
        pass

    def buscar_cliente(self):
        self.carro.buscar_cliente()


class ZonaNorteVeiculoFactory(VeiculoFactory):
    @staticmethod
    def get_carro(tipo: str) -> Veiculo:  # type: ignore
        if tipo == "luxo":
            return CarroLuxo()

        elif tipo == "popular":
            return CarroPopular()

        elif tipo == "moto":
            return Moto()

        assert 0, "Tipo de carro não existe"


class ZonaSulVeiculoFactory(VeiculoFactory):
    @staticmethod
    def get_carro(tipo: str) -> Veiculo:  # type: ignore
        if tipo == 'popular':
            return CarroPopular()

        assert 0, "Veiculo não existe"


if __name__ == "__main__":

    print('ZONA NORTE')
    veiculos_disponiveis_zona_norte = ["luxo", "popular", "moto"]

    for i in range(10):
        carro1 = ZonaNorteVeiculoFactory(choice
                                         (veiculos_disponiveis_zona_norte))
        carro1.buscar_cliente()
        print()

    print('ZONA SUL')

    veiculos_disponiveis_zona_sul = 'popular'

    for i in range(10):
        carro2 = ZonaSulVeiculoFactory(veiculos_disponiveis_zona_sul)
        carro2.buscar_cliente()
        print()
