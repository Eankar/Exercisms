# Globals for the directions
# Change the values as you see fit

NORTH = 1
EAST = 2
SOUTH = 3
WEST = 4

x = 0
y = 0
dir = NORTH


class Robot:
    def __init__(self, direction=NORTH, x_pos=0, y_pos=0):
        global x
        global y
        x = x_pos
        y = y_pos
        global dir
        dir = direction

    def move(direction):
        global dir
        global x
        global y
        for i in direction:
            if i == "R":
                if dir < 4:
                    dir += 1
                else:
                    dir = 1
            elif i == "L":
                if dir > 1:
                    dir -= 1
                else:
                    dir = 4
            elif i == "A":
                if dir == NORTH:
                    x += 1
                elif dir == EAST:
                    y -= 1
                elif dir == SOUTH:
                    x -= 1
                elif dir == WEST:
                    y += 1

    def direction():
        return dir

    def coordinates():
        return (x, y)