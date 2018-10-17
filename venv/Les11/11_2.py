import datetime
vandaag = datetime.datetime.today()
import csv

with open('inloggers.csv', 'a', newline='') as inloggers:
    writer = csv.writer(inloggers, delimiter=';')

    while True:
        naam = input("Wat is je achternaam? ")
        if naam == '':
            break
        voorl = input("Wat zijn je voorletters? ")
        gbdatum = input("Wat is je geboortedatum? ")
        email = input("Wat is je e-mail adres? ")
        datum = vandaag.strftime("%a %d %b %Y at %I:%M:%S")
        writer.writerow((datum, voorl, naam, gbdatum, email))
