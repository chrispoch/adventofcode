import os

#initial
def findDeclarations(text):
    declarations = {}
    for line in text:
        line = line[:-1]
        for i in range(len(line)):
            declarations[line[i]] = True

    return len(declarations.keys())

with open("6.txt") as file:
    total = 0
    groups = 0

    lines = file.readlines() 
    text = []
    for line in lines:
        if len(line) < 2:
            groups = groups + 1
            total = total + findDeclarations(text)
            text = []
        else:
            text.append(line)
    groups = groups + 1
    total = total + findDeclarations(text)

    print(total, groups)

#part2
def findUniqueDeclarations(text):
    declarations = {}
    for line in text:
        line = line[:-1]
        for i in range(len(line)):
            if line[i] in declarations:
                declarations[line[i]] = declarations[line[i]] + 1
            else:
                declarations[line[i]] = 1
    all = []
    for key in declarations:
        if declarations[key] == len(text):
            all.append(key)

    return len(all)

with open("6.txt") as file:
    total = 0
    groups = 0

    lines = file.readlines() 
    text = []
    for line in lines:
        if len(line) < 2:
            groups = groups + 1
            total = total + findUniqueDeclarations(text)
            text = []
        else:
            text.append(line)
    groups = groups + 1
    total = total + findUniqueDeclarations(text)

    print(total, groups)