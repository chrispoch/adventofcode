import os


#initial
def getSeat(text):
    row = 0
    col = 0

    rowCode = text[0:7]
    colCode = text[7:10]

    rowCode = rowCode.replace("F","0")
    rowCode = rowCode.replace("B","1")
    row = int(rowCode, 2)

    colCode = colCode.replace("L","0")
    colCode = colCode.replace("R","1")
    col = int(colCode, 2)
    
    #print(text,rowCode,colCode,str(row),str(col), str(row * 8 + col))

    return row, col

with open("5.txt") as file:
    total = 0
    valid = 0
    invalid = 0

    #print(getSeat("FBFBBFFRLR\n"))

    lines = file.readlines() 
    seats = []
    for line in lines:
        (row, col) = getSeat(line)
        seats.append(row * 8 + col)
        total = total + 1

    seats.sort(reverse=True)
    print(seats[0], total)

#part 2
