"""
Builder é um padrão de criação que tem a intenção de separar
a construção de um objeto complexo da sua representação,
de modo que o mesmo processo de construção possa criar
diferentes representações.

O padrão Builder permite que você construa objetos complexos
passo a passo. O padrão permite que você produza diferentes
tipos e representações de um objeto usando o mesmo código de
construção.

O padrão Builder resolve o problema anti-padrão telescoping
constructor, que ocorre quando o aumento do número de
parâmetros de um construtor torna impossível escrever
sobrecargas para todos eles. O padrão Builder permite que você
construa objetos passo a passo, usando apenas aqueles
construtores que você realmente precisa.
"""
from abc import ABC, abstractmethod


class StringReprMixin:

    def __str__(self):

        params = ', '.join([f'{k}={v}' for k, v in self.__dict__.items()])
        return f'{self.__class__.__name__}({params})'

    def __repr__(self):
        return self.__str__()


class User(StringReprMixin):

    def __init__(self):

        self.firstname = None
        self.lastname = None
        self.age = None
        self.phone_numbers = []
        self.address = []


class IUserBuilder(ABC):
    @property
    @abstractmethod
    def result(self):
        pass

    @abstractmethod
    def add_firstname(self, firstname):
        pass

    @abstractmethod
    def add_lastname(self, lastname):
        pass

    @abstractmethod
    def add_age(self, age):
        pass

    @abstractmethod
    def add_phone(self, phone):
        pass

    @abstractmethod
    def add_address(self, address):
        pass


class UserBuilder(IUserBuilder):

    def __init__(self):
        self.reset()

    def reset(self):
        self._result = User()

    @property
    def result(self):

        return_data = self._result
        self.reset()
        return return_data

    def add_firstname(self, firstname):
        self._result.firstname = firstname

    def add_lastname(self, lastname):
        self._result.lastname = lastname

    def add_age(self, age):
        self._result.age = age

    def add_phone(self, phone):
        self._result.phone_numbers.append(phone)

    def add_address(self, address):
        self._result.address.append(address)


class UserDirector:

    def __init__(self, builder: UserBuilder):

        self.builder = builder  # type: IUserBuilder

    def with_age(self, firstname, lastname, age):

        self.builder.add_firstname(firstname)
        self.builder.add_lastname(lastname)
        self.builder.add_age(age)
        return self.builder.result

    def with_address(self, firstname, lastname, address):

        self.builder.add_firstname(firstname)
        self.builder.add_lastname(lastname)
        self.builder.add_address(address)
        return self.builder.result


if __name__ == "__main__":

    builder = UserBuilder()
    director = UserDirector(builder)
    user = director.with_age("Alfredo", "Gama", 25)
    print(user)

    user = director.with_address("Alfredo", "Gama", "Rua X")
    print(user)

    user2 = director.with_age("Alfredo", "Gama", 25)
    print(user2, user, user == user2)
