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