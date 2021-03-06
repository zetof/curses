import curses
import atexit
from time import sleep

class Screen:

    def __init__(self):
        self.screen = curses.initscr()
        self.screen.keypad(True)
        self.height, self.width = self.screen.getmaxyx()
        curses.noecho()
        curses.cbreak()
        curses.start_color()
        if not curses.has_colors() or not curses.can_change_color() or curses.COLORS != 256:
            self.screen.addstr("Application should be run in a 256 colors capable terminal !!!")
            self.screen.refresh()
            sleep(5)
            self.destroy()
            exit(1)

        atexit.register(self.destroy)

    def available_colors(self):
        return curses.COLORS

    def init_color(self, index, r, g, b):
        curses.init_color(index, r, g, b)

    def init_pair(self, index, color1, color2):
        curses.init_pair(index, color1, color2)

    def print_at(self, x, y, phrase, color):
        self.screen.addstr(y, x, phrase, curses.color_pair(color))

    def refresh(self):
        self.screen.refresh()

    def destroy(self):
        self.screen.keypad(False)
        curses.nocbreak()
        curses.echo()
        curses.endwin()