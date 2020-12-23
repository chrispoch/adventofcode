import os
import sys

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
                rules[num] = [terms[0],terms[1],"&"]
            else:
                if len(terms) == 3:
                    rules[num] = [terms[0],terms[2],"|"]
                else:
                    if len(terms) == 5:
                        rules[num] = [terms[0],terms[1],"&",terms[3],terms[4],"&","|"]
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
    for line in lines:
        if len(line) > 1:
            ruleLines.append(line)
        else:
            break

    rules = rules(ruleLines)
    
    #solve for our rules
    rule0 = rules[0]
    allChars = False
    while not allChars:
        for i in range(len(rule0)):
            if isinstance(rule0[i], int):
                rule0 = rule0[0:i] + rules[rule0[i]] + rule0[i+1:]
        allChars = checkAllChars(rule0)

    print(rule0)