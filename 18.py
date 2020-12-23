import os
import sys

debug = True

fileName = ""
try:
    fileName = sys.argv[1]
    if len(fileName) < 1:
        fileName = "18.txt"
except:
    fileName = "18.txt"
if debug:
    print(fileName)

def solve(lines, precedence):
    solutions = []
    for line in lines:
        #convert to reverse polish notation
        result = ""
        stack = []
        for char in line:
            if char.isdigit():
                result += char
            if char == "(":
                stack.append(char)
            if char == ")":
                while len(stack) > 0 and stack[-1] != "(":
                    result += stack.pop()
                stack.pop()
            if char == "+" or char == "*":
                while len(stack) > 0 and stack[-1] != "(" and precedence[char] <= precedence[stack[-1]]:
                    result += stack.pop()
                stack.append(char)
        while len(stack) > 0:
            result += stack.pop()

        #evaluate reverse polish notation to an int
        stack = []
        for char in result:
            if char.isdigit():
                stack.append(int(char))
            if char == "+" or char == "*":
                result = 0
                two = stack.pop()
                one = stack.pop()
                if char == "+":
                    result = int(one) + int(two)
                else:
                    result = int(one) * int(two)
                stack.append(result)
        solutions.append(stack[0])
    return solutions

with open(fileName) as file:
    lines = file.readlines()

    solutions = solve(lines, {"+":1,"*":1}) 
    if debug:
        print(solutions)
    total = 0
    for sol in solutions:
        total += sol
    print("part 1", total) #part 1

    solutions = solve(lines, {"+":2,"*":1}) 
    if debug:
        print(solutions)
    total = 0
    for sol in solutions:
        total += sol
    print("part 2", total) #part 2