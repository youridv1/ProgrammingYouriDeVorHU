def namen():
    namen = []
    dict = {}
    while True:
        naam = input("Volgende naam: ")
        if len(naam) > 0:
            namen.append(naam)
        else:
            break
    for item in namen:
        if item in dict:
            dict[item] += 1
        else:
            dict[item] = 1
    for key in dict:
        if dict[key] > 1:
            print("Er zijn " + str(dict[key]) + " studenten met de naam " + str(key))
        else:
            print("Er is 1 student met de naam " + str(key))

namen()