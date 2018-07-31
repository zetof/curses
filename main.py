import time
from screen import Screen
from path import Path

path = []
path.append([])
path[0].append('-----')
path[0].append('     ')
path[0].append('     ')
path[0].append('     ')
path[0].append('-----')
path.append([])
path[1].append('|         |')
path[1].append('|         |')
path[1].append('|         |')
path[1].append('|         |')
path.append([])
path[2].append('---------- ')
path[2].append('          |')
path[2].append('          |')
path[2].append('          |')
path[2].append('          |')
path[2].append('|         |')

horizontal = Path(path[0])
vertical = Path(path[1])
right = Path(path[2])

screen = Screen()
screen.initColor(1, 1000, 1000, 0)
screen.initColor(2, 0, 200, 100)
screen.initPair(1, 1, 2)
horizontal.printPath(screen, 10, 10)
right.printPath(screen, 15, 10)
vertical.printPath(screen, 15, 16)
vertical.printPath(screen, 15, 20)
screen.refresh()
time.sleep(2)

