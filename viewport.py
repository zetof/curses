class Viewport:

    VIEW_HEIGHT = 20
    VIEW_WIDTH = 30

    def __init__(self, screen, x, y):
        self.screen = screen
        self.x = x
        self.y = y

    def draw_viewport(self):
        self.screen.print_at(self.x + 1, self.y, '_' * (self.VIEW_WIDTH - 2), 1)
        i = 1
        while i < self.VIEW_HEIGHT:
            self.screen.print_at(self.x, self.y + i, '|' + ' ' * (self.VIEW_WIDTH - 2) + '|', 1)
            i += 1
        self.screen.print_at(self.x, self.y + self.VIEW_HEIGHT, '|' + '_' * (self.VIEW_WIDTH - 2) + '|', 1)

    def draw_common(self):
        i = 2
        while i < 4:
            self.screen.print_at(self.x + i, self.y + i, '\\', 2)
            self.screen.print_at(self.x + self.VIEW_WIDTH - i -1, self.y + i, '/', 2)
            self.screen.print_at(self.x + self.VIEW_WIDTH - i - 1, self.y + self.VIEW_HEIGHT - i + 1, '\\', 2)
            self.screen.print_at(self.x + i, self.y + self.VIEW_HEIGHT - i + 1, '/', 2)
            i += 1

    def draw_dead_end(self, draw_left, draw_right):
        self.screen.print_at(self.x + 7, self.y + 6, '_' * (self.VIEW_WIDTH - 14), 5)
        self.screen.print_at(self.x + 7, self.y + self.VIEW_HEIGHT - 6, '_' * (self.VIEW_WIDTH - 14), 5)
        i = 7
        while i < self.VIEW_HEIGHT - 5:
            if draw_left is True:
                self.screen.print_at(self.x + 6, self.y + i, '|', 5)
            if draw_right is True:
                self.screen.print_at(self.x + self.VIEW_WIDTH - 7, self.y + i, '|', 5)
            i += 1

    def draw_right(self):
        i = 4
        col = 3
        while i < 7:
            self.screen.print_at(self.x + self.VIEW_WIDTH - i -1, self.y + i, '/', col)
            self.screen.print_at(self.x + self.VIEW_WIDTH - i - 1, self.y + self.VIEW_HEIGHT - i + 1, '\\', col)
            i += 1
            col += 1

    def draw_escape_right(self,  draw_left):
        i = 4
        while i < self.VIEW_HEIGHT - 2:
            self.screen.print_at(self.x + self.VIEW_WIDTH - 4, self.y + i, '|', 2)
            i += 1
        if draw_left is True:
            self.screen.print_at(self.x + self.VIEW_WIDTH - 6, self.y + 6, '_' * 2, 5)
            self.screen.print_at(self.x + self.VIEW_WIDTH - 6, self.y + self.VIEW_HEIGHT - 6, '_' * 2, 5)
        else:
            self.screen.print_at(self.x + self.VIEW_WIDTH - 7, self.y + 6, '_' * 3, 5)
            self.screen.print_at(self.x + self.VIEW_WIDTH - 7, self.y + self.VIEW_HEIGHT - 6, '_' * 3, 5)
        if draw_left is True:
            i = 7
            while i < self.VIEW_HEIGHT - 5:
                self.screen.print_at(self.x + self.VIEW_WIDTH - 7, self.y + i, '|', 5)
                i += 1

    def draw_left(self):
        i = 4
        col = 3
        while i < 7:
            self.screen.print_at(self.x + i, self.y + i, '\\', col)
            self.screen.print_at(self.x + i, self.y + self.VIEW_HEIGHT - i + 1, '/', col)
            i += 1
            col += 1

    def draw_escape_left(self, draw_right):
        i = 4
        while i < self.VIEW_HEIGHT - 2:
            self.screen.print_at(self.x + 3, self.y + i, '|', 2)
            i += 1
        if draw_right is True:
            self.screen.print_at(self.x + 4, self.y + 6, '_' * 2, 5)
            self.screen.print_at(self.x + 4, self.y + self.VIEW_HEIGHT - 6, '_' * 2, 5)
        else:
            self.screen.print_at(self.x + 4, self.y + 6, '_' * 3, 5)
            self.screen.print_at(self.x + 4, self.y + self.VIEW_HEIGHT - 6, '_' * 3, 5)

        if draw_right is True:
            i = 7
            while i < self.VIEW_HEIGHT - 5:
                self.screen.print_at(self.x + 6, self.y + i, '|', 5)
                i += 1

    def draw_far_end(self):
        i = 7
        col = 6
        while i < 9:
            self.screen.print_at(self.x + i, self.y + i, '\\', col)
            self.screen.print_at(self.x + self.VIEW_WIDTH - i -1, self.y + i, '/', col)
            self.screen.print_at(self.x + self.VIEW_WIDTH - i - 1, self.y + self.VIEW_HEIGHT - i + 1, '\\', col)
            self.screen.print_at(self.x + i, self.y + self.VIEW_HEIGHT - i + 1, '/', col)
            i += 1
            col += 1

        self.screen.print_at(self.x + 9, self.y + 8, '_' * (self.VIEW_WIDTH - 18), 7)
        self.screen.print_at(self.x + 9, self.y + self.VIEW_HEIGHT - 8, '_' * (self.VIEW_WIDTH - 18), 7)
        i = 9
        while i < self.VIEW_HEIGHT - 7:
            self.screen.print_at(self.x + 8, self.y + i, '|', 7)
            self.screen.print_at(self.x + self.VIEW_WIDTH - 9, self.y + i, '|', 7)
            i += 1

    def go_straight(self):
        self.draw_viewport()
        self.draw_common()
        self.draw_left()
        self.draw_right()
        self.draw_far_end()

    def go_stop(self):
        self.draw_viewport()
        self.draw_common()
        self.draw_left()
        self.draw_right()
        self.draw_dead_end(True, True)

    def go_left(self):
        self.draw_viewport()
        self.draw_common()
        self.draw_escape_left(False)
        self.draw_right()
        self.draw_dead_end(False, True)

    def go_right(self):
        self.draw_viewport()
        self.draw_common()
        self.draw_escape_right(False)
        self.draw_left()
        self.draw_dead_end(True, False)

    def go_t(self):
        self.draw_viewport()
        self.draw_common()
        self.draw_escape_right(False)
        self.draw_escape_left(False)
        self.draw_dead_end(False, False)

    def go_x(self):
        self.draw_viewport()
        self.draw_common()
        self.draw_escape_right(True)
        self.draw_escape_left(True)
        self.draw_far_end()