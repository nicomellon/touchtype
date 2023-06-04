from abc import ABC
from typing import List


class KeyboardLayout(ABC):
    name: str
    top_row: List[str]
    home_row: List[str]
    bottom_row: List[str]


class Colemak(KeyboardLayout):
    name = "colemak"
    top_row = ["q", "w", "f", "p", "g", "j", "l", "u", "y", ";", "[", "]"]
    home_row = ["a", "r", "s", "t", "d", "h", "n", "e", "i", "o", "'", "\\"]
    bottom_row = ["`", "z", "x", "c", "v", "b", "k", "m", ",", ".", "/"]


class Dvorak(KeyboardLayout):
    name = "dvorak"
    top_row = ["'", ",", ".", "p", "y", "f", "g", "c", "r", "l", "/", "="]
    home_row = ["a", "o", "e", "u", "i", "d", "h", "t", "n", "s", "-", "\\"]
    bottom_row = ["`", ";", "q", "j", "k", "x", "b", "m", "w", "v", "z"]


class Qwerty(KeyboardLayout):
    name = "qwerty"
    top_row = ["q", "w", "e", "r", "t", "y", "u", "i", "o", "p", "[", "]"]
    home_row = ["a", "s", "d", "f", "g", "h", "j", "k", "l", ";", "'", "\\"]
    bottom_row = ["`", "z", "x", "c", "v", "b", "n", "m", ",", ".", "/"]
