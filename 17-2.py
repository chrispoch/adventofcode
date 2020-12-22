import os
import copy
import sys

debug = False
iterations = 6

fileName = ""
try:
    fileName = sys.argv[1]
    if len(fileName) < 1:
        fileName = "17.txt"
except:
    fileName = "17.txt"
if debug:
    print(fileName)

cubes = []

def checkNeighbors(x, y, z, w):
    count = 0
    for cube in cubes:
        if (cube[0] >= (x - 1) and cube[0] <= (x + 1) 
        and cube[1] >= (y - 1) and cube[1] <= (y + 1) 
        and cube[2] >= (z - 1) and cube[2] <= (z + 1) 
        and cube[3] >= (w - 1) and cube[3] <= (w + 1) 
        and not (cube[0] == x and cube[1] == y and cube[2] == z and cube[3] == w)):
            count += 1
    return count

def prettyPrint(minX, maxX, minY, maxY, minZ, maxZ, minW, maxW):
    for w in range(minW,maxW+1):
        print("w=",w,end=",")
        for z in range(minZ,maxZ+1):
            print("z=",z)
            for y in range(minY,maxY+1):
                for x in range(minX,maxX+1):
                    if [x,y,z] in cubes:
                        print("#",end="")
                    else:
                        print(".",end="")
                print("")
            print("")

    

with open(fileName) as file:
    minX = 1000
    maxX = 0
    minY = 1000
    maxY = 0
    minZ = 0
    maxZ = 0
    minW = 0
    maxW = 0

    # read in starting content
    lines = file.readlines()
    for y in range(len(lines)):
        for x in range(len(lines[y])):
            if lines[y][x] == "#":
                coord = [x,y,0,0]
                cubes.append(coord)
                if x > maxX:
                    maxX = x
                if x < minX:
                    minX = x
                if y > maxY:
                    maxY = y
                if y < minY:
                    minY = y
    if debug:
        print(0,"------")
        prettyPrint(minX,maxX,minY,maxY,minZ,maxZ,minW,maxW)

    for i in range(iterations):
        c = copy.deepcopy(cubes)
        for cube in cubes:
            #check if it becomes inactive
            neighbors = checkNeighbors(cube[0],cube[1],cube[2],cube[3])
            if neighbors < 2 or neighbors > 3:
                try:
                    c.remove(cube)
                except:
                    pass
                #print("removing",cube)
                
        #check if any neighbors become active
        for x in range(minX-1,maxX+2):
            for y in range(minY-1,maxY+2):
                for z in range(minZ-1,maxZ+2):
                    for w in range(minW-1,maxW+2):
                        if [x,y,z,w] not in cubes and [x,y,z,w] not in c:
                            neighbors = checkNeighbors(x, y, z, w)
                            if neighbors == 3:
                                c.append([x,y,z,w])
                                if x > maxX:
                                    maxX = x
                                if x < minX:
                                    minX = x
                                if y > maxY:
                                    maxY = y
                                if y < minY:
                                    minY = y 
                                if z > maxZ:
                                    maxZ = z
                                if z < minZ:
                                    minZ = z
                                if w > maxW:
                                    maxW = w
                                if w < minW:
                                    minW = w
                                #print("adding",[x,y,z])
        cubes = c
        if debug:
            print(i,"-----")
            prettyPrint(minX,maxX,minY,maxY,minZ,maxZ,minW,maxW)


    print(len(cubes)) #part2

 