filetxt = open("input.txt", "r")
lines = filetxt.readlines()
vars = {}
for i in range(len(lines)):
    print(i)
    lines[i] = lines[i].strip()
print(lines)
for i in lines:
    args = i.split(" ")
    print(args)
    print(vars)
    match args[0]:
        case "Cum":
            if args[1] == "on":
                print(vars.get(args[2]))
        
    match args[1]:
        case "is":
            vars.update({args[0]: args[2]})