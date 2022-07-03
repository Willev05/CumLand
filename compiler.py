filetxt = open("input.txt", "r")
lines = filetxt.readlines()
vars = {}
inIf = False
for i in range(len(lines)):
    lines[i] = lines[i].strip()
for line in lines:
    args = line.split(" ")
    if inIf == False:
        match args[0]:
            case "Cum":
                if args[1] == "on":
                    print(vars.get(args[2]))
                elif args[1] == "in":
                    vars.update({args[2]: input()})
            
            case "If":
                if args[2] == "is":
                    if len(args) > 4:
                        if args[3] == "not":
                            if vars.get(args[1]) == vars.get(args[4]):
                                inIf = True
                        elif args[3] == "bigger":
                            if vars.get(args[1]) < vars.get(args[4]):
                                inIf = True
                        elif args[3] == "smaller":
                            if vars.get(args[1]) > vars.get(args[4]):
                                inIf = True
                    else:
                        if vars.get(args[1]) > vars.get(args[3]):
                            inIf = True
            
            case "End":
                if args[1] == "if":
                    inIf = False
                    inIfFailed = False

        match args[1]:
            case "is":
                val = None
                bad = True
                try: 
                    val = float(args[2])
                    bad = False
                except:
                    bad = True
                    #vars.update({args[0]: args[2]})
                if bad:
                    if args[2] == "True":
                        val = True
                    elif args[2] == "False":
                        val = False
                    else:
                        val = args[2]
                        if len(args) > 3:
                            for i in args[3:]:
                                val = val + " " + i
                vars.update({args[0]: val})
            case "plus":
                val = 0
                if args[3] == "is":
                    try:
                        val = vars.get(args[0]) + vars.get(args[2])
                    except:
                        exit("One of the variables is not a float/int!", line)
                    try:
                        vars.update({args[4]: val})
                    except:
                        exit("Missing variable name in line", line)
                else:
                    exit("Invalid syntax (missing is) in line", line)
            case "minus":
                val = 0
                if args[3] == "is":
                    try:
                        val = vars.get(args[0]) - vars.get(args[2])
                    except:
                        exit("One of the variables is not a float/int!", line)
                    try:
                        vars.update({args[4]: val})
                    except:
                        exit("Missing variable name in line",line)
                else:
                    exit("Invalid syntax (missing is) in line", line)
            case "times":
                val = 0
                if args[3] == "is":
                    try:
                        val = vars.get(args[0]) * vars.get(args[2])
                    except:
                        exit("One of the variables is not a float/int!", line)
                    try:
                        vars.update({args[4]: val})
                    except:
                        exit("Missing variable name in line",line)
                else:
                    exit("Invalid syntax (missing is) in line", line)
            case "divided":
                val = 0
                if args[3] == "is":
                    try:
                        val = vars.get(args[0]) / vars.get(args[2])
                    except:
                        exit("One of the variables is not a float/int!", line)
                    try:
                        vars.update({args[4]: val})
                    except:
                        exit("Missing variable name in line",line)
                else:
                    exit("Invalid syntax (missing is) in line", line)
    else:
        if args[0] == "End" and args[1] == "if":
            inIf = False
print(vars)
#:)