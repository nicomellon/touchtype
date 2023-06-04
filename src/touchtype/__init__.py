import curses
import sys

from . import home
from . import tutorial


def main() -> None:
    """Entry point for the application script."""
    try:
        curses.wrapper(home.start)
    except KeyboardInterrupt:
        sys.exit(0)
