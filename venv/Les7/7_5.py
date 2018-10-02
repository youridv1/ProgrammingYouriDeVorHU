def gemiddelde(zin):
    szin= zin.split(sep = ' ')
    total = 0
    count = 0
    for word in szin:
        total += len(word)
        count += 1
    res = total / count
    return res

print(gemiddelde(input("Geef een willekeurige zin: ")))


