lyst = eval(input("Geef lijst met minimaal 10 strings: "))
newlist = []
for string in lyst:
    if len(string) == 4:
        newlist.append(string)

print("De nieuw-gemaakte lijst met alle vier-letter strings is:" + str(newlist))

