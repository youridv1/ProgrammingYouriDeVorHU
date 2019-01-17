def linsearch(lijst, getal):
    while len(lijst) > 0:
        if lijst[0] == getal:
            print(getal, "gevonden")
            lijst.pop(0)
            break
        else:
            lijst.pop(0)
            linsearch(lijst, getal)

linsearch([5, 2, 3, 4], 4)