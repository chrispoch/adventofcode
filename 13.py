import os
import sys

debug = False
fileName = ""
try:
    fileName = sys.argv[1]
    if len(fileName) < 1:
        fileName = "13.txt"
except:
    fileName = "13.txt"
print(fileName)

with open(fileName) as file:
    time = int(file.readline())
    note = file.readline()
    note2 = note.replace(",x","")
    buses = note2.split(",")
    for i in range(len(buses)):
        buses[i] = int(buses[i])
    leaves = []

    for i in range(len(buses)):
        leaves.append(time + buses[i] - (time % buses[i]))
    
    min = leaves[0]
    mini = 0
    for i in range(len(leaves)):
        if leaves[i] < min:
            min = leaves[i]
            mini = i
    wait = leaves[mini] - time
    print(buses[mini], wait, buses[mini] * wait)

    #part 2
    print("Part 2")
    buses = note.split(",")
    #print(buses)
    for i in range(len(buses)):
        if buses[i] == "x":
            buses[i] = 0
        else:
            #print(buses[i])
            buses[i] = int(buses[i])
    leaves = []
    for bus in buses:
        leaves.append(0)

    time = 0
    step = 1
    #influenced by https://gist.github.com/joshbduncan/65f810fe821c7a3ea81a1f5a444ea81e
    """Since you must find departure times for each bus based off of the previous bus schedule (which is based on the previous bus and so on...), all following buses must depart at a multiple of all previous buses departures since they have to stay in the order provided.

Step Progression
1 * 7 = 7
7 * 13 = 91
91 * 59 = 5369
5369 * 31 = 166439

Then you just need to add the cumulative time (t) and the minute offset for each bus in the list to get the final answer."""
    p2 = [(int(i), j) for j, i in enumerate(buses) if i != 0]
    for bus, offset in p2:
        while (time + offset) % bus != 0:
            time += step
        step *= bus

    print(time)

