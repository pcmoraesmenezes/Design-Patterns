"""
Bridge é um padrão de proejto estrutural que tem a intenção
de desacoplar uma abstração da sua implementação, de modo
que as duas possam variar e evoluir independentemente.

O Bridge é um padrão de projeto muito popular em aplicações
escritas em Java. A implementação do padrão depende muito
do uso de recursos de reflexão da linguagem. Em Python, a
implementação do padrão é mais simples pois a linguagem já
possui um suporte nativo ao paradigma de programação
orientada a objetos.

"""
from __future__ import annotations
from abc import ABC, abstractmethod


class IRemoteControl(ABC):

    @abstractmethod
    def increase_volume(self) -> None:
        pass

    @abstractmethod
    def decrease_volume(self) -> None:
        pass

    @abstractmethod
    def power(self) -> None:
        pass


class RemoteControl(IRemoteControl):

    def __init__(self, device: IDevice) -> None:
        self._device = device

    def increase_volume(self) -> None:
        self._device.volume += 10

    def decrease_volume(self) -> None:
        self._device.volume -= 10

    def power(self) -> None:
        self._device.power = not self._device.power


class IDevice(ABC):

    @property
    @abstractmethod
    def volume(self) -> int:
        pass

    @volume.setter
    @abstractmethod
    def volume(self, volume: int) -> None:
        pass

    @property
    @abstractmethod
    def power(self) -> bool:
        pass

    @power.setter
    @abstractmethod
    def power(self, power: bool) -> None:
        pass


class TV(IDevice):

    def __init__(self) -> None:
        self._volume = 0
        self._power = False
        self._name = self.__class__.__name__

    @property
    def volume(self) -> int:
        return self._volume

    @volume.setter
    def volume(self, volume: int) -> None:

        if not self.power:
            print(f'Turn {self._name} on first')
            return

        if volume in range(0, 101):
            self._volume = volume

    @property
    def power(self) -> bool:
        return self._power

    @power.setter
    def power(self, power: bool) -> None:
        self._power = power


if __name__ == "__main__":
    tv = TV()
    remote_control = RemoteControl(tv)

    remote_control.power()
    print('TV is on:', tv.power)
    remote_control.increase_volume()
    print('TV volume:', tv.volume)
    remote_control.decrease_volume()
    print('TV volume:', tv.volume)
    remote_control.power()
    print('TV is on:', tv.power)
    remote_control.increase_volume()
