"""
Adapter é um padrão de projeto estrutural que tem a intenção de
permitir que duas classes que seriam incompatíveis trabalhem em
conjunto através de um adaptador.

- O Adapter permite que você insira código de terceiros em uma
aplicação sem precisar alterar o código de terceiros ou a aplicação.
- O Adapter também pode ser usado como uma forma de reutilizar
classes antigas em uma nova aplicação.
- O Adapter funciona como um tradutor entre duas entidades.
- O Adapter é um padrão de projeto bastante comum em Python.
"""
from abc import ABC, abstractmethod


class IControl(ABC):

    @abstractmethod
    def top(self) -> None:
        pass

    @abstractmethod
    def down(self) -> None:
        pass

    @abstractmethod
    def left(self) -> None:
        pass

    @abstractmethod
    def right(self) -> None:
        pass


class Control(IControl):

    def top(self) -> None:
        print("Moving top")

    def down(self) -> None:
        print("Moving down")

    def left(self) -> None:
        print("Moving left")

    def right(self) -> None:
        print("Moving right")


class NewControl:

    def move_top(self) -> None:
        print("Moving top")

    def move_down(self) -> None:
        print("Moving down")

    def move_left(self) -> None:
        print("Moving left")

    def move_right(self) -> None:
        print("Moving right")


class Adapter:

    def __init__(self, new_control: NewControl) -> None:

        self.new_control = new_control

    def top(self) -> None:
        self.new_control.move_top()

    def down(self) -> None:
        self.new_control.move_down()

    def left(self) -> None:
        self.new_control.move_left()

    def right(self) -> None:
        self.new_control.move_right()


class Adapter2(Control, NewControl):

    def top(self) -> None:
        self.move_top()

    def down(self) -> None:
        self.move_down()

    def left(self) -> None:
        self.move_left()

    def right(self) -> None:
        self.move_right()


if __name__ == "__main__":

    new_control = NewControl()
    control_object = Adapter(new_control)

    control_object.top()
    control_object.down()
    control_object.left()
    control_object.right()

    print()

    control_object2 = Adapter2()
    control_object2.top()
    control_object2.down()
    control_object2.left()
    control_object2.right()
