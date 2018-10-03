studentencijfers = [ [95, 92, 86],[66, 75, 54],[89, 72, 100],[34, 0, 0] ]

def gemiddelde_per_student(studentencijfers):
    antw = []
    for i in studentencijfers:
        count = 0
        som = 0
        for j in i:
           count += 1
           som += int(j)
        gemiddelde = som / count
        antw.append(gemiddelde)
    return antw

def gemiddelde_van_alle_studenten(studentencijfers):
    antw = []
    count = 0
    som = 0
    for i in studentencijfers:
        for j in i:
            count += 1
            som += int(j)
    antw = som / count
    return antw



print(gemiddelde_per_student(studentencijfers))
print(gemiddelde_van_alle_studenten(studentencijfers))
