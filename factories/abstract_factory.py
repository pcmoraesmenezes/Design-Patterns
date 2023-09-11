"""
Abstract Factory é um padrão de criação que fornece uma interface para criar
familias de objetos relacionados ou dependentes sem especificar suas classes
concretas.

Abstract Factory permite que um sistema seja independente de como seus objetos
são criados, compostos ou representados.

Uma diferença importante entre Factory Method e Abstract Factory é que o
Factory Method usa herança, enquanto Abstract Factory usa composição.

Principio: Programe para uma interface, não para uma implementação.
"""
from abc import ABC, abstractmethod


class VeiculoLuxo(ABC):
    @abstractmethod
    def buscar_cliente(self) -> None:
        pass


class VeiculoPopular(ABC):
    @abstractmethod
    def buscar_cliente(self) -> None:
        pass


class CarroLuxoZN(VeiculoLuxo):
    def buscar_cliente(self) -> None:
        print("Carro de luxo da ZONA NORTE está buscando o cliente...")


class CarroPopularZN(VeiculoPopular):
    def buscar_cliente(self) -> None:
        print("Carro popular da ZONA NORTE está buscando o cliente...")


class MotoLuxoZN(VeiculoLuxo):
    def buscar_cliente(self) -> None:
        print("Moto Luxo da ZONA NORTE está buscando o cliente...")


class MotoPopularZN(VeiculoPopular):
    def buscar_cliente(self) -> None:
        print("Moto Popular da ZONA NORTE está buscando o cliente...")


class CarroLuxoZS(VeiculoLuxo):
    def buscar_cliente(self) -> None:
        print("Carro de luxo da ZONA SUL está buscando o cliente...")


class CarroPopularZS(VeiculoPopular):
    def buscar_cliente(self) -> None:
        print("Carro popular da ZONA SUL está buscando o cliente...")


class MotoLuxoZS(VeiculoLuxo):
    def buscar_cliente(self) -> None:
        print("Moto Luxo da ZONA SUL está buscando o cliente...")


class MotoPopularZS(VeiculoPopular):
    def buscar_cliente(self) -> None:
        print("Moto Popular da ZONA SUL está buscando o cliente...")

# Fabrica


class VeiculoFactory:
    @staticmethod
    @abstractmethod
    def get_carro_luxo() -> VeiculoLuxo:  # type: ignore
        pass

    @staticmethod
    @abstractmethod
    def get_carro_popular() -> VeiculoPopular:  # type: ignore
        pass

    @staticmethod
    @abstractmethod
    def get_moto_popular() -> VeiculoPopular:  # type: ignore
        pass

    @staticmethod
    @abstractmethod
    def get_moto_luxo() -> VeiculoLuxo:  # type: ignore
        pass


class ZonaNorteVeiculoFactory(VeiculoFactory):
    @staticmethod
    def get_carro_luxo() -> VeiculoLuxo:  # type: ignore
        return CarroLuxoZN()

    @staticmethod
    def get_carro_popular() -> VeiculoPopular:  # type: ignore
        return CarroPopularZN()

    @staticmethod
    def get_moto_popular() -> VeiculoPopular:  # type: ignore
        return MotoPopularZN()

    @staticmethod
    def get_moto_luxo() -> VeiculoLuxo:  # type: ignore
        return MotoLuxoZN()


class ZonaSulVeiculoFactory(VeiculoFactory):

    @staticmethod
    def get_carro_luxo() -> VeiculoLuxo:  # type: ignore
        return CarroLuxoZS()

    @staticmethod
    def get_carro_popular() -> VeiculoPopular:  # type: ignore
        return CarroPopularZS()

    @staticmethod
    def get_moto_popular() -> VeiculoPopular:  # type: ignore
        return MotoPopularZS()

    @staticmethod
    def get_moto_luxo() -> VeiculoLuxo:  # type: ignore
        return MotoLuxoZS()


class Cliente:
    def busca_clientes_zn(self):
        for factory in [ZonaNorteVeiculoFactory()]:
            carro_popular = factory.get_carro_popular()
            carro_popular.buscar_cliente()

            carro_luxo = factory.get_carro_luxo()
            carro_luxo.buscar_cliente()

            moto_popular = factory.get_moto_popular()
            moto_popular.buscar_cliente()

            moto_luxo = factory.get_moto_luxo()
            moto_luxo.buscar_cliente()

    def busca_clientes_zs(self):
        for factory in [ZonaSulVeiculoFactory()]:
            carro_popular = factory.get_carro_popular()
            carro_popular.buscar_cliente()

            carro_luxo = factory.get_carro_luxo()
            carro_luxo.buscar_cliente()

            moto_popular = factory.get_moto_popular()
            moto_popular.buscar_cliente()

            moto_luxo = factory.get_moto_luxo()
            moto_luxo.buscar_cliente()


if __name__ == "__main__":
    clientezn = Cliente()
    print('ZONA NORTE: \n')
    clientezn.busca_clientes_zn()

    print('\nZONA SUL: \n')
    clientezs = Cliente()
    clientezs.busca_clientes_zs()
