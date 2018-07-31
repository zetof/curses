import curses

class Screen:

    def __init__(self):

        self.screen = curses.initscr()
        curses.noecho()
        curses.cbreak()
        self.screen.keypad(True)

    def printit(self, phrase):
        self.screen.addstr(0, 0, phrase, curses.A_REVERSE)
        self.screen.refresh()

    def destroy(self):
        curses.nocbreak()
        self.screen.keypad(False)
        curses.echo()
        curses.endwin()
