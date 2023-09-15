from __future__ import annotations
from abc import ABC, abstractmethod


class Sound:
    def __init__(self) -> None:
        self.mode: PlayMode = RadioMode(self)
        self.playing = 0

    def change_mode(self, mode: PlayMode) -> None:
        self.playing = 0
        self.mode = mode

    def press_next(self) -> None:
        self.mode.press_next()
        print(self)

    def press_previous(self) -> None:
        print(self)
        self.mode.press_previous()

    def __str__(self) -> str:
        return f'Playing: {self.playing}'


class PlayMode(ABC):

    def __init__(self, sound: Sound) -> None:
        self.sound = sound

    @abstractmethod
    def press_next(self) -> None:
        pass

    @abstractmethod
    def press_previous(self) -> None:
        pass


class RadioMode(PlayMode):

    def press_next(self) -> None:
        self.sound.playing += 100

    def press_previous(self) -> None:
        self.sound.playing -= 100 if self.sound.playing >= 100 else 0


class MusicMode(PlayMode):

    def press_next(self) -> None:
        self.sound.playing += 1

    def press_previous(self) -> None:
        self.sound.playing -= 1 if self.sound.playing >= 1 else 0


if __name__ == "__main__":
    sound = Sound()
    sound.press_next()
    sound.press_next()

    sound.change_mode(MusicMode(sound))
    sound.press_next()
    sound.press_next()
    sound.press_previous()
    sound.press_previous()
