import os
import itertools
import datetime

fileName = "10.txt"
max = -1

def validateList(adapters):
    valid = True
    if adapters == None:
        return False
    if len(adapters) < 2:
        return False
    if adapters[0] != 0:
        return False
    if adapters[-1] != max:
        return False

    for i in range(len(adapters) - 1):
        if adapters[i + 1] - adapters[i] > 3:
            valid = False
            break
    return valid

def makeId(list):
    result = ""
    if len(list) == 0:
        return ""
    
    for item in list:
        result = result + str(item) + ","
    return result[:-1]

print(datetime.datetime.now())
with open(fileName) as file:
    numbers = file.readlines()
    for i in range(len(numbers)):
        numbers[i] = int(numbers[i])
    #add start and end
    numbers.append(0)
    numbers.sort()
    numbers.append(numbers[-1] + 3)

    diff1 = 0
    diff3 = 0
    numbers.sort()
    for i in range(len(numbers) - 1):
        if numbers[i + 1] - numbers[i] == 1:
            diff1 = diff1 + 1
        else:
            if numbers[i + 1] - numbers[i] == 3:
                diff3 = diff3 + 1
        i = i + 1
    print(diff1, diff3, diff1 * diff3)
    #part 2
    max = numbers[-1]
    validOptions = {}
    
    L = 0
    for L in range(len(numbers)):
        item = itertools.combinations(numbers, L + 1)
        for combo in item:
            comboList = list(combo)
            #comboList.sort()
            #print(comboList)
            if validateList(comboList):
                validOptions[makeId(comboList)] = True
                #print("Match")
        L = L + 1
    print(len(validOptions))
print(datetime.datetime.now())