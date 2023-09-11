"""
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
    @staticmethod
    def get_carro(tipo: str) -> Veiculo:  # type: ignore
        if tipo == "luxo":
            return CarroLuxo()

        elif tipo == "popular":
            return CarroPopular()

        elif tipo == "moto":
            return Moto()

        assert 0, "Tipo de carro não existe"


if __name__ == "__main__":
    carros_disponiveis = ["luxo", "popular", "moto"]

    for i in range(10):
        carro = VeiculoFactory.get_carro(choice(carros_disponiveis))
        carro.buscar_cliente()
        print()
