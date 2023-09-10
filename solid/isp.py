"""
Interface segregation principle
"""
from abc import ABC, abstractmethod


class Client(ABC):

    @abstractmethod
    def get_cpf(self): pass

    @abstractmethod
    def get_cnpj(self): pass


class PhysicalPerson(Client):
    def get_cpf(self):
        pass

    def get_cnpj(self):
        pass


class LegalPerson(Client):
    def get_cpf(self):
        pass

    def get_cnpj(self):
        pass

# watch out the necessity of implementetion for cnpj method
# in PhysicalPerson class and the necessity of method cpf in
# Legal Person class.
# This break the Interface Segregation Principle, because the client
# is forced to need a interface
