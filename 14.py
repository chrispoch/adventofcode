import os
import sys
import itertools

debug = False
fileName = ""
try:
    fileName = sys.argv[1]
    if len(fileName) < 1:
        fileName = "14.txt"
except:
    fileName = "14.txt"
print(fileName)

memory = {}
#for i in range(2 ** 36):
#    memory.append(0)

with open(fileName) as file:
    commands = file.readlines()

    mask = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
    for command in commands:
        if command[0:4] == "mask":
            mask = command[7:43]
        else:
            if len(mask) != 36:
                print("!!!!!Bad mask!!!!!")

            index = command[4:command.find("]")]
            inValue = command[command.find("=") + 2:]
            value = bin(int(inValue)).replace("0b","")

            if len(value) < 36:
                numAppend = 36 - len(value)
                append = ""
                for i in range(numAppend):
                    append = append + "0"
                value = append + value

            #compute real value
            real = ""
            for i in range(36):
                if mask[i] == "1" or mask[i] == "0":
                    real = real + mask[i]
                else:
                    real = real + value[i]
            intVal = int(real, 2)
            memory[index] = intVal

    #get sum of memory
    total = 0
    for item in memory:
        total += memory[item]
    print(total)

    #part 2
    memory = {}
    mask = "000000000000000000000000000000000000"
    for command in commands:
        if command[0:4] == "mask":
            mask = command[7:43]
            #print("msk",mask)
        else:
            if len(mask) != 36:
                print("!!!!!Bad mask!!!!!")

            index = bin(int(command[4:command.find("]")])).replace("0b","")
            value = int(command[command.find("=") + 2:])

            if len(index) < 36:
                numAppend = 36 - len(index)
                append = ""
                for i in range(numAppend):
                    append = append + "0"
                index = append + index
            #print("pre", index, int(index, 2))
            addresses = []
            newIndex = ""
            for i in range(36):
                if mask[i] == "1" or mask[i] == "X":
                    newIndex = newIndex + mask[i]
                else:
                    newIndex = newIndex + index[i]
            index = newIndex

            floating = mask.count("X")
            perms = itertools.product([0, 1], repeat = floating)
            #print("pst",index)
            for perm in list(perms):
                addr = index
                for i in range(floating):
                    addr = addr.replace("X",str(perm[i]),1)
                #print("itr",addr,int(addr,2),"*")
                addresses.append(int(addr,2))
            if floating == 0:
                #print(index, int(index,2), "~")
                addresses.append(int(index,2))
            
            #print(addresses)
            for address in addresses:
                memory[address] = value

    #get sum of memory
    #print(memory)
    total = 0
    for item in memory:
        total += memory[item]
    print(total)