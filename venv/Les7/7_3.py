regels = len(open('Kaartnummers.txt').readlines())

max = 0
count = 0
infile = open('Kaartnummers.txt')
for line in infile:
    currentline = line.split(",")
    currentline[-1] = currentline[-1].strip()
    huidige = int(currentline[0])
    count +=1
    if huidige > max:
        max = huidige
        regelnr = count

print("Deze file telt " + str(regels) + " regels.")
print("Het grootste kaartnummer is: " + str(max) + " en dat staat op regel " + str(regelnr))




