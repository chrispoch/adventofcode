import os
import copy

debug = False
fileName = "12.txt"
with open(fileName) as file:
    heading = 0 #east
    x = 0
    y = 0

    directions = file.readlines()
    for direction in directions:
        ins = direction[0]
        value = int(direction[1:])

        if ins == "N":
            y = y + value
        if ins == "S":
            y = y - value
        if ins == "E":
            x = x + value
        if ins == "W":
            x = x - value
        if ins == "L":
            heading = (heading - value) % 360
        if ins == "R":
            heading = (heading + value) % 360
        if ins == "F":
            if heading % 90 != 0:
                print("!!!!!!!!!!We didn't expect to be here!!!!!!!!!!")
            if heading == 0:
                x = x + value
            if heading == 180:
                x = x - value
            if heading == 90:
                y = y - value
            if heading == 270:
                y = y + value
        if debug:
            print(direction, ins, value, x, y, heading)
    print(x, y, abs(x) + abs(y))

    print("Part 2")
    #part 2
    heading = 0 #east
    wx = 10
    wy = 1
    sx = 0
    sy = 0

    for direction in directions:
        ins = direction[0]
        value = int(direction[1:])

        if ins == "N":
            wy = wy + value
        if ins == "S":
            wy = wy - value
        if ins == "E":
            wx = wx + value
        if ins == "W":
            wx = wx - value
        if ins == "L":
            n = int((value % 360) / 90)
            for i in range(n):
                r = wy
                wy = wx
                wx = r * -1
        if ins == "R":
            n = int((value % 360) / 90)
            for i in range(n):
                r = wy
                wy = wx * -1
                wx = r
        if ins == "F":
            sx = sx + (value * wx)
            sy = sy + (value * wy)
        if debug:
            print(direction, ins, value, wx, wy, sx, sy)
    print(wx, wy, sx, sy, abs(sx) + abs(sy))
