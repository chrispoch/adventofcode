import os
import itertools
import datetime

fileName = "10.txt"

def validateList(adapters, min, max):
    valid = True
    if adapters == None:
        return False
    if len(adapters) < 2:
        return False
    if adapters[0] != min:
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
    unskippable = []
    unskippable.append(0)

    for i in range(len(numbers)):
        if i > 0 and (numbers[i] - numbers[i - 1]) == 3:
            unskippable.append(i)
        else:
            if (i + 1) < len(numbers):
                big = numbers[i + 1]
                little = numbers[i]
                if (big - little) == 3:
                    unskippable.append(i)

    problems = []
    for i in range(1, len(unskippable)):
        pair = [unskippable[i - 1], unskippable[i]]
        problems.append(pair)
    solutions = []
    for i in range(len(problems)):
        solutions.append(0)

    #work each problem and save its solution
    for i in range(len(problems)):
        mini = problems[i][0]
        maxi = problems[i][1]
        if maxi - mini == 1:
            solutions[i] = 1
        else:
            validOptions = {}
            workSet = numbers[mini:maxi + 1]

            L = 0
            for L in range(len(workSet)):
                item = itertools.combinations(workSet, L + 1)
                for combo in item:
                    comboList = list(combo)
                    if validateList(comboList, workSet[0], workSet[-1]):
                        validOptions[makeId(comboList)] = True
                L = L + 1
            solutions[i] = len(validOptions)
    total = 1
    for item in solutions:
        total *= item
    print(total)
print(datetime.datetime.now())