"""
Command tem a intenção de encapsular uma solicitação como um
objeto, desta forma permitindo parametrizar clientes com diferentes
solicitações, enfileirar ou fazer o registro (log) de solicitações e
suportar operações que podem ser desfeitas.

O padrão Command é muito útil quando precisamos desacoplar um objeto
que envia uma solicitação de um objeto que sabe como executá-la.

O padrão Command é uma solução elegante para todos esses problemas.
Ele encapsula uma solicitação como um objeto, o que o torna portátil
e parametrizável. O objeto que invoca a solicitação não precisa se
preocupar com os detalhes de como a solicitação será executada.
"""

from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Dict


class Light:
    """Receiver"""
    def __init__(self, name: str, room_name: str) -> None:
        self.name = name
        self.room_name = room_name
        self.color = 'Default color'

    def on(self) -> None:
        print(f'\nLight {self.name} on in {self.room_name} with {self.color} color')  # noqa

    def off(self) -> None:
        print(f'\nLight {self.name} off in {self.room_name}')

    def change_color(self, color: str) -> None:
        self.color = color
        print(f'\nLight {self.name} in {self.room_name} with {self.color} color')  # noqa


class ICommand(ABC):
    """Interface Command"""
    @abstractmethod
    def execute(self) -> None:
        pass

    @abstractmethod
    def undo(self) -> None:
        pass


class LightOnCommand(ICommand):
    """Concrete Command"""
    def __init__(self, light: Light) -> None:
        self.light = light

    def execute(self) -> None:
        self.light.on()

    def undo(self) -> None:
        self.light.off()


class LightChangeColorCommand(ICommand):
    """Concrete Command"""
    def __init__(self, light: Light, color: str) -> None:
        self.light = light
        self.color = color
        self._old_color = light.color

    def execute(self) -> None:
        self.light.change_color(self.color)

    def undo(self) -> None:
        self.light.change_color(self._old_color)


class RemoteController:
    """Invoker"""
    def __init__(self) -> None:
        self._buttons: Dict[str, ICommand] = {}

    def button_add_command(self, name: str, command: ICommand) -> None:
        self._buttons[name] = command

    def button_execute(self, name: str) -> None:

        try:
            self._buttons[name].execute()
        except KeyError:
            print(f'\nButton {name} not found...')

    def button_undo(self, name: str) -> None:

        try:
            self._buttons[name].undo()
        except KeyError:
            print(f'\nButton {name} not found...')


if __name__ == "__main__":
    bedroom_light = Light('Bedroom_light', 'Bedroom')
    kitchen_light = Light('Kitchen_light', 'Kitchen')

    bedroom_light_on = LightOnCommand(bedroom_light)
    kitchen_light_on = LightOnCommand(kitchen_light)

    remote_controller = RemoteController()
    remote_controller.button_add_command('btn_1', bedroom_light_on)
    remote_controller.button_add_command('btn_2', kitchen_light_on)

    remote_controller.button_execute('btn_1')
    remote_controller.button_execute('btn_2')

    remote_controller.button_undo('btn_1')
    remote_controller.button_undo('btn_2')

    bedroom_light.change_color('Blue')
    bedroom_light_on = LightOnCommand(bedroom_light)

    remote_controller.button_add_command('btn_3', bedroom_light_on)
    remote_controller.button_execute('btn_3')

    remote_controller.button_undo('btn_3')

    remote_controller.button_undo('btn_4')

    """
    Observer tem a intenção de definir uma dependência um-para-muitos
    entre objetos, de maneira que quando um objeto muda o estado,
    todos os seus dependentes são notificados e atualizados
    automaticamente.

    O padrão Observer é muito popular em aplicações escritas em Java.
    A implementação do padrão depende muito do uso de recursos de
    reflexão da linguagem. Em Python, a implementação do padrão é
    mais simples pois a linguagem já possui um suporte nativo ao
    paradigma de programação orientada a objetos.
    """
