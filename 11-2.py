import os
import copy

printOut = False
printIter = False

#part2
lines = []
def checkAdjacent(row, col):
    if lines[row][col] == ".":
        return 0
    count = 0
    #print("************")

    #check left
    checkR = row
    checkC = col - 1
    while checkC > 0 and lines[checkR][checkC] == ".":
        checkC = checkC - 1
    if checkC >= 0 and lines[checkR][checkC] == "#":
        if printOut:
            print(row, col, checkR, checkC, "left")
        count = count + 1

    #check right
    checkR = row
    checkC = col + 1
    while checkC < len(lines[checkR]) and lines[checkR][checkC] == ".":
        checkC = checkC + 1
    if checkC < len(lines[checkR]) and lines[checkR][checkC] == "#":
        if printOut:
            print(row, col, checkR, checkC, "right")
        count = count + 1

    #check up
    checkR = row - 1
    checkC = col
    while checkR > 0 and lines[checkR][checkC] == ".":
        checkR = checkR - 1
    if checkR >= 0 and lines[checkR][checkC] == "#":
        if printOut:
            print(row, col, checkR, checkC, "up")
        count = count + 1

    #check down
    checkR = row + 1
    checkC = col
    while checkR < len(lines) and lines[checkR][checkC] == ".":
        checkR = checkR + 1
    if checkR < len(lines) and lines[checkR][checkC] == "#":
        if printOut:
            print(row, col, checkR, checkC, "down")
        count = count + 1

    #check left-up
    checkR = row - 1
    checkC = col - 1
    while checkC > 0 and checkR > 0 and lines[checkR][checkC] == ".":
        checkC = checkC - 1
        checkR = checkR - 1
    if checkC >= 0 and checkR >= 0 and lines[checkR][checkC] == "#":
        if printOut:
            print(row, col, checkR, checkC, "left-up")
        count = count + 1

    #check right-up
    checkR = row - 1
    checkC = col + 1
    while checkC < len(lines[checkR]) and checkR > 0 and lines[checkR][checkC] == ".":
        checkC = checkC + 1
        checkR = checkR - 1
    if checkC < len(lines[checkR]) and checkR >= 0 and lines[checkR][checkC] == "#":
        if printOut:
            print(row, col, checkR, checkC, "right-up")
        count = count + 1

    #check left-down
    checkR = row + 1
    checkC = col - 1
    while checkC > 0 and checkR < len(lines) and lines[checkR][checkC] == ".":
        checkC = checkC - 1
        checkR = checkR + 1
    if checkC >= 0 and checkR < len(lines) and lines[checkR][checkC] == "#":
        if printOut:
            print(row, col, checkR, checkC, "left-down")
        count = count + 1

    #check right-down
    checkR = row + 1
    checkC = col + 1   
    while checkR < len(lines) and checkC < len(lines[checkR]) and lines[checkR][checkC] == ".":
        checkC = checkC + 1
        checkR = checkR + 1
    #print(row, col, checkR, checkC, len(lines),len(lines[checkR]))
    if checkR < len(lines) and checkC < len(lines[checkR]) and lines[checkR][checkC] == "#":
        if printOut:
            print(row, col, checkR, checkC, "right-down")
        count = count + 1
    if printOut:
        print(row, col, "Count", count)
    return count

def printSeats():
    for line in lines:
        print(line)

with open("11.txt") as file:
    lines = file.readlines()
    for i in range(len(lines)):
        if lines[i][-1] == "\n":
            lines[i] = lines[i][0:-1]


    iteration = 0
    changed = True
    if printIter:
        print("---------",iteration)
        printSeats()
    while changed == True:
        workingSeats = copy.deepcopy(lines)
        changed = False
        iteration = iteration + 1

        for r in range(len(lines)):
            colLen = len(lines[r])
            for c in range(colLen):
                count = checkAdjacent(r, c)
                myLine = workingSeats[r]
                if count == 0 and myLine[c] == "L":
                    myLine = myLine[:c] + "#" + myLine[c + 1:]
                    workingSeats[r] = myLine
                    changed = True
                if count > 4 and myLine[c] == "#":
                    myLine = myLine[:c] + "L" + myLine[c + 1:]
                    workingSeats[r] = myLine
                    changed = True
                c = c + 1
            r = r + 1
        lines = copy.deepcopy(workingSeats)
        if printIter:
            print("---------",iteration)
            printSeats()
            print(str(changed))
    occupiedCount = 0
    for line in lines:
        occupiedCount = occupiedCount + line.count("#")
    print(occupiedCount)