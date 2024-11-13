x = "jhdoenceefsa"
if len(x) < 10:
    print("String too short!")
else:
    if x[8] == "e" and (x[7] == "d" or x[9] == "f"):
        print("Version A")
    else:
        print("Version B")