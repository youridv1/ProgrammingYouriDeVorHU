def gemiddelde(zin):
    zin = zin.strip()
    zin = zin.strip('.')
    zin = zin.split(sep = ' ')
    total = 0
    count = 0
    for word in zin:
        total += len(word)
        count += 1
    res = total / count
    return res

print(gemiddelde(input("Geef een willekeurige zin: ")))


