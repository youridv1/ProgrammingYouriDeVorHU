import csv

def schrijver():
    with open('voorraad.csv', 'w', newline='') as voorraad:
        writer = csv.writer(voorraad, delimiter=';')
        writer.writerow(('Artikelnummer', 'Artikelcode', 'Naam', 'Voorraad', 'Prijs'))
        while True:
            Nummer = input('Geef het Artikelnummer: ')
            if Nummer == '':
                break
            Code = input('Geef de Artikelcode: ')
            Naam = input('Geef de naam: ')
            Voorraad = input('Geef de hoeveelheid in voorraad: ')
            Voorraad = int(Voorraad)
            Prijs = input('Geef de prijs: ')
            Prijs = float(Prijs)
            writer.writerow((Nummer, Code, Naam, Voorraad, Prijs))

def lezer():
    with open('voorraad.csv', 'r') as voorraad:
        reader = csv.DictReader(voorraad, delimiter=';')
        prijs = 0
        for row in reader:
            if float(row['Prijs']) > prijs:
                prijs = float(row['Prijs'])
                naam = row['Naam']
        print('Het duurste artikel is', naam, 'en die kost', prijs, 'Euro')
        voorraad2 = 999999
        nummer = 0
    with open('voorraad.csv', 'r') as voorraad:
        reader = csv.DictReader(voorraad, delimiter=';')
        for row in reader:
            if int(row['Voorraad']) < voorraad2:
                voorraad2 = int(row['Voorraad'])
                nummer = row['Artikelnummer']
        print('Er zijn slechts', voorraad2, 'exemplaren in voorraad van het product', nummer)
    with open('voorraad.csv', 'r') as voorraad:
        reader = csv.DictReader(voorraad, delimiter=';')
        totaal = 0
        for row in reader:
            totaal += int(row['Voorraad'])
        print('In totaal hebben wij', totaal, 'producten in ons magazijn liggen')

