
name = "Guido Van Rossum"

dictList = {}

for var in name:
    if var in dictList:
        print("I am a IfBlock")
        dictList[var] += 1
    else:
        print("I am ElseBlcok")
        dictList[var] = 1

print(dictList)