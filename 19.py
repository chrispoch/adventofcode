import os
import sys
import re

debug = True

fileName = ""
try:
    fileName = sys.argv[1]
    if len(fileName) < 1:
        fileName = "19.txt"
except:
    fileName = "19.txt"
if debug:
    print(fileName)

def rules(lines):
    rules = {}
    for line in lines:
        #convert to reverse polish notation
        vals = line[:-1].split(":")
        num = int(vals[0])
        terms = vals[1][1:].split(" ")
        for i in range(len(terms)):
            try:
                intVal = int(terms[i])
                terms[i] = intVal
            except:
                terms[i] = terms[i].replace('"','')

        if len(terms) == 1:
            rules[num] = [terms[0]]
        else:
            if len(terms) == 2:
                rules[num] = ["(",terms[0],terms[1],")"]
            else:
                if len(terms) == 3:
                    rules[num] = ["(",terms[0],"|",terms[2],")"]
                else:
                    if len(terms) == 5:
                        rules[num] = ["(",terms[0],terms[1],"|",terms[3],terms[4],")"]
                    else:
                        print("Error len(terms)=",len(terms))
    return rules

def checkAllChars(list):
    allChars = True
    for item in list:
        if isinstance(item, int):
            allChars = False
            break
    return allChars

with open(fileName) as file:
    lines = file.readlines()
    ruleLines = []
    messages = []
    isRule = True
    for line in lines:
        if len(line) > 1:
            if isRule:
                ruleLines.append(line)
            else:
                messages.append(line)
        else:
            isRule = False
            

    rules = rules(ruleLines)
    
    #solve for our rules
    rule0 = rules[0]
    allChars = False
    while not allChars:
        for i in range(len(rule0)):
            if isinstance(rule0[i], int):
                rule0 = rule0[0:i] + rules[rule0[i]] + rule0[i+1:]
        allChars = checkAllChars(rule0)

    #make regex string
    strRule0 = "^"
    for item in rule0:
        strRule0 += str(item)
    strRule0 += "$"
    if debug:
        print(strRule0)
    part1Pattern = re.compile(strRule0)

    #check remaining strings
    matchLength = 0
    matches = 0
    possiblePart2 = []
    for msg in messages:
        if part1Pattern.match(msg) != None:
            matches += 1
            matchLength = len(msg)
        else:
            if len(msg) > matchLength:
                possiblePart2.append(msg)

    print(matches)

    #implement part 2 changes
    #rules[8] = ["(",42,"|",42,8,")"] # was 42; now produces 42 42 42 42...
    #rules[11] = ["(",42,31,"|",42,11,31,")"] # was 42 31; now produces 42 ... 31 ... 
    #rule 0 is 8 11 so produces 42 n * 31 m, n > m

    #need to find 42 and 31
    rule42 = rules[42]
    allChars = False
    while not allChars:
        for i in range(len(rule42)):
            if isinstance(rule42[i], int):
                rule42 = rule42[0:i] + rules[rule42[i]] + rule42[i+1:]
        allChars = checkAllChars(rule42)
    strRule42 = ""
    for item in rule42:
        strRule42 += str(item)

    rule31 = rules[31]
    allChars = False
    while not allChars:
        for i in range(len(rule31)):
            if isinstance(rule31[i], int):
                rule31 = rule31[0:i] + rules[rule31[i]] + rule31[i+1:]
        allChars = checkAllChars(rule31)
    strRule31 = ""
    for item in rule31:
        strRule31 += str(item)

    #check possible part 2
    strRule8 = strRule42 + '+'
    strRule11 = r'(' + '|'.join([f'{strRule42}{{{n}}}{strRule31}{{{n}}}' for n in range(1,5)]) + ')'
    strRule0 = '^' + strRule8 + strRule11 + '$'

    part2Pattern = re.compile(strRule0)

    #check remaining strings
    matches = 0
    for msg in messages:
        if part2Pattern.match(msg) != None:
            matches += 1

    print(matches)