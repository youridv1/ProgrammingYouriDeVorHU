invoer = "5-9-7-1-7-8-3-2-4-8-7-9"
invoer = invoer.strip('"')
invoer = invoer.split(sep = '-')
invoer = sorted(invoer)
count = 0
som = 0
for getal in invoer:
    getal = int(getal)
    count += 1
    som += getal
gemiddelde = som / count
max = max(invoer)
min = min(invoer)

print("Gesorteerde list van ints: " + str(invoer))
print("Grootste getal: " + str(max) + " en Kleinste getal: " + str(min))
print("Aantal getallen: " + str(count) + " en Som van de getallen: " + str(som))
print("Gemiddelde: " + str(gemiddelde))

