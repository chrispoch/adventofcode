import os


#initial
with open("3.txt") as file:
    lines = file.readlines() 
    count = 0
    trees = 0
    miss = 0
    xpos = 0

    for line in lines:
        count = count + 1
        line = line[:-1] #remove newline
        
        if line[xpos % len(line)] == "#":
            trees = trees + 1
            line = line[:xpos % len(line)] + "X" + line[xpos % len(line) + 1:]
        else:
            miss = miss + 1
            line = line[:xpos % len(line)] + "O" + line[xpos % len(line) + 1:]
        xpos = xpos + 3
        #print(line)
    print(trees)

#part2
def findTrees(x, y, lines):
    trees = 0
    xpos = 0
    lineCount = 0

    for line in lines:
        line = line[:-1] #remove newline

        if lineCount % y == 0:        
            if line[xpos % len(line)] == "#":
                trees = trees + 1
                line = line[:xpos % len(line)] + "X" + line[xpos % len(line) + 1:]
            else:
                line = line[:xpos % len(line)] + "O" + line[xpos % len(line) + 1:]
            xpos = xpos + x
        lineCount = lineCount + 1
        #print(line)
    return trees

r1d1 = findTrees(1,1,lines)
r3d1 = findTrees(3,1,lines)
r5d1 = findTrees(5,1,lines)
r7d1 = findTrees(7,1,lines)
r1d2 = findTrees(1,2,lines)
#print(str(r1d1),str(r3d1),str(r5d1),str(r7d1),str(r1d2))
print(str(r1d1 * r3d1 * r5d1 * r7d1 * r1d2))


