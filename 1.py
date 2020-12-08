import os

with open("1.txt") as file:
    nums = file.readlines() 
    for num1 in nums:
        for num2 in nums:
            if int(num1) + int(num2) == 2020:
                print(num1, num2, str(int(num1)*int(num2)),sep=" ")
    print("Part 2")
    for num1 in nums:
        for num2 in nums:
            for num3 in nums:
                if int(num1) + int(num2) + int(num3) == 2020:
                    print(num1, num2, num3, str(int(num1)*int(num2)*int(num3)),sep=" ")