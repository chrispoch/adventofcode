import os

fileName = "9.txt"
preamble = 25
part1Num = -1
part1Index = -1
with open(fileName) as file:
    numbers = file.readlines()
    for i in range(len(numbers)):
        numbers[i] = int(numbers[i])
    i = preamble
    isValid = True
    while i  < len(numbers) and isValid:
        checkValue = int(numbers[i])
        isValid = False
        for j in range(preamble):
            for k in range(preamble):
                if j != k and checkValue == (int(numbers[i - j - 1]) + int(numbers[i - k - 1])):
                    isValid = True
                    break
                k = k + 1
            if isValid:
                break
            j = j + 1
        if isValid:
            i = i + 1
    print(numbers[i], i, len(numbers))
    part1Num = int(numbers[i])
    part1Index = i

    #part 2
    indexMin = -1
    indexMax = -1
    for startIndex in range(part1Index):
        sum = 0
        for i in range(part1Index - startIndex):
            if sum < part1Num:
                sum = sum + int(numbers[startIndex + i])
            else:
                break
            i = i + 1
        if sum == part1Num:
            indexMin = startIndex
            indexMax = startIndex + i
            break
        startIndex = startIndex + 1
    
    newRange = numbers[indexMin:indexMax]
    newRange.sort()
    print(newRange[0] + newRange[-1])
