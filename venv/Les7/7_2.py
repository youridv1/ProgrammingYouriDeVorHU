infile = open('Kaartnummers.txt')
for line in infile:
    currentline = line.split(",")
    currentline[-1] = currentline[-1].strip()
    print(currentline[-1] + "heeft kaartnummer: " + currentline[0])

