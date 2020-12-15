import os
import copy

#initial
lines = []
def checkAdjacent(row, col):
    if lines[row][col] == ".":
        return 0
    count = 0
    #print("************")
    for r in range(row - 1, row + 2):
        for c in range (col - 1, col + 2):
            try :
                #print(r,c,row,col,str(len(lines)),str(len(lines[r])),lines[r][c],end="")
                if not(r == row and c == col) and (r > -1 and r < len(lines)) and (c > -1 and c < len(lines[r])) and lines[r][c] == "#":
                    count = count + 1
                    #print("!!!")
                #else:
                    #print("")
            except:
                pass
    #print(count)
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
    #print("---------",iteration)
    #printSeats()
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
                if count > 3 and myLine[c] == "#":
                    myLine = myLine[:c] + "L" + myLine[c + 1:]
                    workingSeats[r] = myLine
                    changed = True
                c = c + 1
            r = r + 1
        lines = copy.deepcopy(workingSeats)
        #print("---------",iteration)
        #printSeats()
        #print(str(changed))
    occupiedCount = 0
    for line in lines:
        occupiedCount = occupiedCount + line.count("#")
    print(occupiedCount)