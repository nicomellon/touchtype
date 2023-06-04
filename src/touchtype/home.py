import curses
import curses.panel

from .colors import Colors
from .config import Config
from .layouts import Colemak, Dvorak, Qwerty
from .tutorial import start as start_tutorial

config = Config()


def init_colors() -> Colors:
    curses.use_default_colors()
    curses.init_pair(1, curses.COLOR_GREEN, -1)
    curses.init_pair(2, curses.COLOR_RED, -1)
    return Colors(curses.color_pair(1), curses.color_pair(2))


def start(screen: curses.window) -> None:
    colors = init_colors()
    screen.clear()
    screen.addstr("Touchtype")
    screen.move(2, 0)
    screen.addstr("t -> Tutorial")
    screen.move(4, 0)
    screen.addstr("l -> Select keyboard layout")
    screen.refresh()

    while True:
        match screen.getkey():
            case "l":
                select_layout(screen)
            case "t":
                start_tutorial(screen)


def select_layout(screen: curses.window) -> None:
    screen.clear()
    screen.addstr("c -> Colemak")
    screen.move(2, 0)
    screen.addstr("d -> Dvorak")
    screen.move(4, 0)
    screen.addstr("q -> Qwerty")
    screen.refresh()
    match screen.getkey():
        case "c":
            config.layout = Colemak()
        case "d":
            config.layout = Dvorak()
        case "q":
            config.layout = Qwerty()
        
