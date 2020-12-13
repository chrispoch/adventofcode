import os
import copy

fileName = "8.txt"
with open(fileName) as file:
    accumulator = 0
    visited = {}
    code = file.readlines()
    i = 0
    while i  < len(code):
        try:
            if i in list(visited):
                visited[i] = visited[i] + 1
                break
            else:
                visited[i] = 1
            
            op = code[i][0:3]
            val = int(code[i][4:-1])
            #print(code[i][0:-1], op, val)
            if op == "acc":
                accumulator = accumulator + val
            if op == "jmp":
                i = i + val
            else:
                i = i + 1
        except:
            print(i, "Something went wrong!!!!!!!!!!!!!!!!!")
print(accumulator)

#part 2
with open(fileName) as file:
    success = False
    realCode = file.readlines()
    for l in range(len(realCode)):
        #print(l)
        code = copy.deepcopy(realCode)
        op = code[l][0:3]
        if op == "nop" or op == "jmp":
            if op == "jmp":
                code[l] = code[l].replace("jmp","nop")
            else:
                code[l] = code[l].replace("nop","jmp")

            #run the program again
            accumulator = 0
            visited = {}
            i = 0
            stop = False
            while i  < len(code) and not stop:
                try:
                    if i in list(visited):
                        visited[i] = visited[i] + 1
                        stop = True
                        break
                    else:
                        visited[i] = 1
                    
                    op = code[i][0:3]
                    val = int(code[i][4:-1])
                    #print(code[i][0:-1], op, val)
                    if op == "acc":
                        accumulator = accumulator + val
                    if op == "jmp":
                        i = i + val
                    else:
                        i = i + 1
                except:
                    print(i, "Something went wrong!!!!!!!!!!!!!!!!!")
            if stop == False:
                success = True
                print("Part 2 success",l,accumulator)
                break
print(accumulator)