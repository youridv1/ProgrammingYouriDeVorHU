regels = len(open('Kaartnummers.txt').readlines())

max = 0
count = 1
infile = open('Kaartnummers.txt')
for line in infile:
    currentline = line.split(",")
    currentline[-1] = currentline[-1].strip()
    huidige = int(currentline[0])
    if huidige > max:
        max = huidige
        count += 1
print("Deze file telt " + str(regels) + " regels.")




