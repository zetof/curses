class Path:

    def __init__(self, elements):
        self.width = len(elements[0])
        self.height = len(elements)
        self.elements = elements

    def printPath(self, screen, x, y):
        screen.printAt(0, 0 , str(self.width), 1)
        screen.printAt(0, 1 , str(self.height), 1)
        i = 0;
        for element in self.elements:
            screen.printAt(x, y + i, element, 1)
            i += 1

