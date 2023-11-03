names = input()
newName = ""
i = names.find(" ")
Y = names[0:i]
P = names[i+1:]
if Y[-1] == "e":
    newName = Y + "x" + P
elif Y[-1] in "aiou":
    newName = Y[0:-1] + "ex" + P
elif Y[-2:] == "ex": 
    newName = Y + P
else:
    newName = Y + "ex" + P
print(newName)