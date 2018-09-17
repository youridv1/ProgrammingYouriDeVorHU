loon_input = input('Wat verdien je per uur? ')
loon = float(loon_input)
Aantal_uren_input = input('Hoeveel uur heb je gewerkt? ')
Aantal_uren = float(Aantal_uren_input)
Salaris = loon * Aantal_uren
Salarisstr = str(Salaris)
Aantal_urenstr = str(Aantal_uren)
line = Aantal_urenstr + ' ' + 'uur werken levert' + ' ' + Salarisstr + ' ' + 'Euro op.'
print(line)
