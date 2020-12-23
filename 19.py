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
    matches = 0
    for msg in messages:
        if part1Pattern.match(msg) != None:
            matches += 1
    print(matches)

    #implement part 2 changes
    rules[8] = ["(",42,"|",42,8,")"]
    rules[11] = ["(",42,31,"|",42,11,31,")"]
    