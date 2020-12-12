import os

fileName = "7.txt"
with open(fileName) as file:
    rules = {}
    total = 0
    text = file.readlines()
    for rule in text:
        total = total + 1
        myColor = rule[0:rule.find(" bag")]
        i = rule.find("contain") + 7
        others = rule[i:-2]
        others = others.replace("bags","")
        others = others.replace("bag","")
        others = others.split(",")
        for i in range(len(others)):
            others[i] = others[i][3:-1]
        rules[myColor] = others
        #print(myColor,others)
    #print(total, len(rules)) #proves rules are for unique colors
    containsGold = {}
    containsGold["shiny gold"] = True
    #for rule in rules:
    #    if "shiny gold" in rules[rule]:
    #        containsGold[rule] = True
    size = 0
    while size != len(containsGold):
        size = len(containsGold)
        for foundColor in list(containsGold):
            for newColor in rules:
                if foundColor in rules[newColor]:
                    containsGold[newColor] = True
        #print(size,"----------------",len(containsGold))
        #print(containsGold.keys())
    print(len(containsGold) - 1) #remove shiny gold

#part 2
rules = {}
total = 0

def insidePackages(color):
    if len(rules[color]) == 0:
        return 0
    count = 0
    for sub in rules[color].keys():
        #print ("---",sub,rules[color][sub],insidePackages(sub))
        count = count + (rules[color][sub] * (insidePackages(sub) + 1))
    #print(color,count)
    return count


with open(fileName) as file:
#    text = file.readlines()
    for rule in text:
        total = total + 1
        myColor = rule[0:rule.find(" bag")]
        i = rule.find("contain") + 7
        others = rule[i:-2]
        others = others.replace("bags","")
        others = others.replace("bag","")
        others = others.split(",")
        contents = {}
        for other in others:
            try:
                contents[other[3:-1]] = int(other[1])
            except:
                pass
        rules[myColor] = contents
        #print(myColor,others)
    #print(total, len(rules)) #proves rules are for unique colors

    #print("------------")
    #print(rules)
    #print("------------")
    insideGold = {}
    for color in rules["shiny gold"]:
        insideGold[color] = rules["shiny gold"][color]

    #size = 0
    #while size != len(insideGold):
    #    size = len(insideGold)
    #    for foundColor in list(insideGold):
    #        for newColor in rules[foundColor].keys():
    #            insideGold[newColor] = rules[foundColor][newColor]

        #print(size,"----------------",len(containsGold))
        #print(containsGold.keys())
    packages = insidePackages("shiny gold")
    #for item in insideGold.keys():
    #    packages = packages + insideGold[item]
    print(packages)