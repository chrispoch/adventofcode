start = [1,20,11,6,12,0]
said1 = -1
said2 = start[0]
val = {}

#for i in range(2020):     #part1
for i in range(30000000):  #part2
    said1 = said2
    if i < len(start):
        said2 = start[i]
    else:
        if said1 not in val.keys():
            said2 = 0
            #print("notfound")
        else:
            #last = max(loc for loc, val in enumerate(said[0:-1]) if val == said[-1])
            #print("*",i,val[said])
            #print("found",i, said2, val[said1])
            said2 = i - 1 - val[said1]
            #print("found",i,val[said])
            #print(said[-1])
    val[said1] = i - 1
    #print(said1)
    
    #print(val)

print(said2)