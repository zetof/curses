import curses
from time import sleep
from screen import Screen
from viewport import Viewport

screen = Screen()
viewport = Viewport(screen, 0, 1)

screen.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLACK)
screen.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)

viewport.go_straight()
screen.refresh()
sleep(1)
viewport.go_stop()
screen.refresh()
sleep(1)
viewport.go_left()
screen.refresh()
sleep(1)
viewport.go_right()
screen.refresh()
sleep(1)
viewport.go_t()
screen.refresh()
sleep(1)
viewport.go_x()
screen.refresh()
sleep(5)
