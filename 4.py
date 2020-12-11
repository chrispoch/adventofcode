import os


#initial
def validatePassport(pp):
    if len(pp) < 7:
        return False
    fields = pp.keys()
    if "byr" not in fields:
        return False
    if "iyr" not in fields:
        return False
    if "eyr" not in fields:
        return False
    if "hgt" not in fields:
        return False
    if "hcl" not in fields:
        return False
    if "ecl" not in fields:
        return False
    if "pid" not in fields:
        return False
    return True

def makePassport(text):
    pp = {}
    for line in text:
        line = line[:-1]
        pairs = line.split(" ")
        for pair in pairs:
            (key, val) = pair.split(":")
            pp[key] = val

    return pp

with open("4.txt") as file:
    total = 0
    valid = 0
    invalid = 0

    lines = file.readlines() 
    text = []
    for line in lines:
        if len(line) < 2:
            total = total + 1
            pp = makePassport(text)
            if validatePassport(pp):
                valid = valid + 1
            else:
                invalid = invalid + 1
            text = []
        else:
            text.append(line)
    total = total + 1
    pp = makePassport(text)
    if validatePassport(pp):
        valid = valid + 1
    else:
        invalid = invalid + 1

    print(valid, invalid, total)

#part2
def validatePassport2(pp):
    #print("------")
    try:
        if len(pp) < 7:
            #print("too few")
            return False
        fields = pp.keys()
        if "byr" not in fields or int(pp["byr"]) < 1920 or int(pp["byr"]) > 2002:
            #print("byr")
            #print(pp["byr"])
            return False
        if "iyr" not in fields or int(pp["iyr"]) < 2010 or int(pp["iyr"]) > 2020:
            #print("iyr")
            #print(pp["iyr"])
            return False
        if "eyr" not in fields or int(pp["eyr"]) < 2020 or int(pp["eyr"]) > 2030:
            #print("eyr")
            #print(pp["eyr"])
            return False
        if "hgt" not in fields:
            #print("hgt")
            return False
        if pp["hgt"][-2:] == "cm":
            #print("cm")
            if int(pp["hgt"][:-2]) < 150 or int(pp["hgt"][:-2]) > 193:
                #print("cm-bad")
                #print(pp["hgt"])
                return False
        else:
            if pp["hgt"][-2:] == "in":
                #print("in")
                if int(pp["hgt"][:-2]) < 59 or int(pp["hgt"][:-2]) > 76:
                    #print("in-bad")
                    #print(pp["hgt"])
                    return False
            else:
                #print("hgt unit")
                #print(pp["hgt"])
                return False
        if "hcl" not in fields or pp["hcl"][0] != "#" or len(pp["hcl"]) != 7 or int(pp["hcl"][1:], 16) < 0:
            #print("hcl")
            #print(pp["hcl"])
            return False
        if "ecl" not in fields or pp["ecl"] not in ["amb","blu","brn","gry","grn","hzl","oth"]:
            #print("ecl")
            #print(pp["ecl"])
            return False
        if "pid" not in fields or len(pp["pid"]) != 9 or int(pp["pid"]) < 0 or int(pp["pid"]) > 999999999:
            #print("pid")
            #print(pp["pid"])
            return False
        #print("*Valid")
        #print("========")
        #print(pp["pid"],len(pp["pid"]))
        return True
    except:
        return False

with open("4.txt") as file:
    total = 0
    valid = 0
    invalid = 0

    lines = file.readlines() 
    text = []
    for line in lines:
        if len(line) < 2:
            total = total + 1
            #print("------" + str(total))
            #print(text)
            pp = makePassport(text)
            result = validatePassport2(pp)
            if result:
                valid = valid + 1
            else:
                invalid = invalid + 1
            #try:
            #    print(str(total),pp["pid"],str(result), sep=",")
            #except:
            #    print(str(total), "missing", str(result), sep=",")
            
            text = []
        else:
            text.append(line)
    total = total + 1
    pp = makePassport(text)
    if validatePassport2(pp):
        valid = valid + 1
    else:
        invalid = invalid + 1

    print(valid, invalid, total)