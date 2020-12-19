import os
from collections import defaultdict
import itertools

debug = False
fileName = ""
try:
    fileName = sys.argv[1]
    if len(fileName) < 1:
        fileName = "16.txt"
except:
    fileName = "16.txt"
if debug:
    print(fileName)

fields = {}
invalidValues = {}

def validateFields(values, min1, max1, min2, max2):
    valid = True
    for value in values:
        if (value < min1 or value > max1) and (value < min2 or value > max2):
            valid = False
    return valid

with open(fileName) as file:
    minVal = 1000
    maxVal = 0
    for i in range(1000):
        invalidValues[i] = True

    line = file.readline()
    while line != "\n":
        allowed = []
        name = line[:line.find(":")]
        ranges = line[line.find(":") + 2:].split("or")
        for r in ranges:
            pair = r.split("-")
            pair[0] = int(pair[0])
            pair[1] = int(pair[1])
            allowed.append(pair[0])
            allowed.append(pair[1])
            if pair[0] < minVal:
                minVal = pair[0]
            if pair[1] > maxVal:
                maxVal = pair[1]
            for i in range(pair[0],pair[1] + 1):
                try:
                    del invalidValues[i]
                except:
                    pass
        if debug:
            print(allowed)
        fields[name] = allowed
        line = file.readline()
    if debug:
        print(invalidValues)

    myTicket = []
    otherTickets = []

    while line != "your ticket:\n":
        line = file.readline()
    line = file.readline()
    myTicket = line.split(",")
    for i in range(len(myTicket)):
        myTicket[i] = int(myTicket[i])
    
    while line != "nearby tickets:\n":
        line = file.readline()
    line = file.readline()
    while len(line) > 1:
        ticket = line.split(",")
        for i in range(len(ticket)):
            ticket[i] = int(ticket[i])
        otherTickets.append(ticket)
        line = file.readline()

    #validate tickets
    validTickets = []
    validTickets.append(myTicket)
    errorRate = 0
    for ticket in otherTickets:
        valid = True
        for field in ticket:
            if field in invalidValues:
                valid = False
                errorRate += field
        if valid:
            validTickets.append(ticket)
    print(errorRate) #part1

    #get all the values per field
    fieldUse = []
    for i in range(len(myTicket)):
        values = {}
        for j in range(len(validTickets)):
            values[validTickets[j][i]] = True
        fieldUse.append(values)

    fieldNames = defaultdict(list)
    for i in range(len(fields)):
        fieldNames[i] = []
    for field in fields.keys():
        for i in range(len(fields)):
            ranges = fields[field]
            if validateFields(fieldUse[i],ranges[0],ranges[1],ranges[2],ranges[3]):
                fieldNames[i].append(field)
    #print(fieldNames)

    possibilities = 0
    for field in fieldNames:
        possibilities += len(fieldNames[field])

    while len(fields) < possibilities:
        if debug:
            print("-------",len(fields), possibilities)
        targetDeletion = []
        for field in fieldNames:
            if len(fieldNames[field]) == 1:
                targetDeletion.append(fieldNames[field][0])

        for field in fieldNames:
            if len(fieldNames[field]) == 1:
                pass
            else:
                newFields = []
                for name in fieldNames[field]:
                    if name not in targetDeletion:
                        newFields.append(name)
                fieldNames[field] = newFields
        if debug:
            print(fieldNames)

        possibilities = 0
        for field in fieldNames:
            possibilities += len(fieldNames[field])
    if debug:
        print("*****", fieldNames)

    myVal = 1
    for i in range(len(fieldNames)):
        if "departure" in fieldNames[i][0]:
            myVal *= myTicket[i]
    print(myVal) #part2
