def toon_aantal_kluizen_vrij():
    kluizen = open('kluizen.txt')
    kluizenlines = kluizen.readlines()
    kluizen.close()
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
    kluizen.close()
    for line in kluizenlines:
        line = line.split(';')
        gevondenkluizen.append(int(line[0]))
    kluizenlist = [x for x in kluizenlist if x not in gevondenkluizen]
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
    kluizen.close()

def kluis_openen():
    nummer = input("Geef uw kluisnummer: ")
    code = input("Geef uw code: ")
    combinatie = nummer + ';' + code + '\n'
    kluizenlist = []
    wachtwoorden = []
    kluizen = open('kluizen.txt')
    kluizenlines = kluizen.readlines()
    kluizen.close()
    if combinatie in kluizenlines:
        print("Kluis nummer " + str(nummer) + " is nu open.")
    else:
        print("Kluisnummer en/of code incorrect.")
    kluizen.close()

def kluis_teruggeven():
    nummer = input("Geef uw kluisnummer: ")
    code = input("Geef uw code: ")
    combinatie = nummer + ';' + code + '\n'
    kluizenlist = []
    wachtwoorden = []
    kluizen = open('kluizen.txt')
    kluizenlines = kluizen.readlines()
    kluizen.close()
    if combinatie in kluizenlines:
        kluizenlines = [x for x in kluizenlines if x not in combinatie]
        kluizen = open('kluizen.txt', 'w')
        for i in kluizenlines:
            kluizen.write(i)
        print("De kluis is nu weer vrij.")
    else:
        print("Kluisnummer en/of code incorrect.")
    kluizen.close()


def bagage():
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
        print(
            "Fout: U kunt alleen kiezen uit de getallen 1 t/m 4.\nHet programma wordt afgelosten.\nProbeer het opnieuw.")
    bagage()

bagage()