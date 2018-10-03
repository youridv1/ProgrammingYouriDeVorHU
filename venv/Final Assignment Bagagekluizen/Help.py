def toon_aantal_kluizen_vrij():
    kluizen = open('kluizen.txt')
    kluizenlines = kluizen.readlines()
    count = 0
    for line in kluizenlines:
        count += 1
    aantal = 12 - int(count)
    res = "Er zijn nog " + str(aantal) + " kluizen vrij."
    return res

def nieuwe_kluis():
    gevondenkluizen = []
    kluizenlist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    kluizen = open('kluizen.txt')
    kluizenlines = kluizen.readlines()
    for line in kluizenlines:
        line = line.split(';')
        gevondenkluizen.append(int(line[0]))
    kluizenlist = [x for x in kluizenlist if x not in gevondenkluizen]
    kluizen.close()
    if len(kluizenlist) > 0:
        code = input("Voer een toegangscode van minimaal 4 tekens in voor het later openen van de kluis: ")
    else:
        print("Sorry, alle kluizen zijn in gebruik.")
    if len(code) >= 4:
        kluizen = open('kluizen.txt', 'a')
        kluizen.write(str(min(kluizenlist)) + ';' + str(code) + '\n')
        print('U hebt kluis nummer ' + str(min(kluizenlist)))
    else:
        print("Sorry, die code is niet lang genoeg.")

def kluis_openen():
    nummer = input("Geef uw kluisnummer: ")
    code = input("Geef uw code: ")
    kluizenlist = []
    wachtwoorden = []
    kluizen = open('kluizen.txt')
    kluizenlines = kluizen.readlines()
    kluizen.close()
    for line in kluizenlines:
        line = line.split(';')
        line[1] = line[1].strip()
        kluizenlist.append(line[0])
        wachtwoorden.append(line[1])
    if nummer in kluizenlist and code in wachtwoorden:
        print("Kluis nummer " + str(nummer) + " is nu open.")
    else:
        print("Kluisnummer en/of code incorrect.")

def kluis_teruggeven():
    nummer = input("Geef uw kluisnummer: ")
    code = input("Geef uw code: ")
    kluizenlist = []
    wachtwoorden = []
    kluizen = open('kluizen.txt')
    kluizenlines = kluizen.readlines()
    kluizen.close()
    for line in kluizenlines:
        line = line.split(';')
        line[1] = line[1].strip()
        kluizenlist.append(line[0])
        wachtwoorden.append(line[1])
    if nummer in kluizenlist and code in wachtwoorden:
        combinatie = [nummer + ';' + code + '\n']
        kluizenlines = [x for x in kluizenlines if x not in combinatie]
        kluizen = open('kluizen.txt', 'w')
        for i in kluizenlines:
            kluizen.write(i)
        print("De kluis is nu weer vrij.")
    else:
        print("Kluisnummer en/of code incorrect.")












keuze = int(input("1: Ik wil weten hoeveel kluizen er nog vrij zijn\n"
      "2: Ik wil een nieuwe kluis\n"
      "3: Ik wil even iets uit mijn kluis halen\n"
      "4: Ik geef mijn kluis terug\n"
      "Toets de gewenste keuze in: "))

if keuze > 0 and keuze < 5:
    if keuze == 1:
        print(toon_aantal_kluizen_vrij())
    elif keuze == 2:
        nieuwe_kluis()
    elif keuze == 3:
        kluis_openen()
    elif keuze == 4:
        kluis_teruggeven()
else:
    print("Fout: U kunt alleen kiezen uit de getallen 1 t/m 4.\nHet programma wordt afgelosten.\nProbeer het opnieuw.")