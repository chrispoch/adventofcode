import os


#initial
with open("2.txt") as file:
    lines = file.readlines() 
    total = 0
    valid = 0
    invalid = 0

    for line in lines:
        total = total + 1

        sep = line.find("-")
        space = line.find(" ")
        min = int(line[0:sep])
        max = int(line[sep + 1:space])
        letter = line[space + 1]
        password = line[space + 4:]

        found = password.count(letter)
        if found >= min and found <= max:
            valid = valid + 1
        else:
            invalid = invalid + 1
    print(total, valid, invalid)

#part2
    total = 0
    valid = 0
    invalid = 0

    for line in lines:
        total = total + 1

        sep = line.find("-")
        space = line.find(" ")
        pos1 = int(line[0:sep]) - 1
        pos2 = int(line[sep + 1:space]) - 1
        letter = line[space + 1]
        password = line[space + 4:]
        #print (line, str(pos1), str(sep), str(pos2), str(space), letter, password)

        if (password[pos1] == letter or password[pos2] == letter) and (password[pos1] != password[pos2]):
            valid = valid + 1
        else:
            invalid = invalid + 1
    print(total, valid, invalid)