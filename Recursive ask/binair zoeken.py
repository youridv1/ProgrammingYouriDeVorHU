def binsearch(lijst, getal):
    midden = len(lijst) // 2
    if lijst[midden] == getal:
        print("gevonden")
    elif lijst[midden] > getal:
        lijst = lijst[:midden]
        binsearch(lijst, getal)
    else:
        lijst = lijst[midden:]
        binsearch(lijst, getal)

binsearch([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5)