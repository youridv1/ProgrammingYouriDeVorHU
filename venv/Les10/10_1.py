Bruin = set(['Boxtel', 'Best', 'Beukenlaan', 'Eindhoven', 'Helmond \'t Hout', 'Helmond', 'Helmond Brouwhuis', 'Deurne'])
Groen = set(['Boxtel', 'Best', 'Beukenlaan', 'Eindhoven', 'Geldrop', 'Heeze', 'Weert'])

Beide = Bruin.intersection(Groen)
print(Beide)

Verschil = Bruin.difference(Groen)
print(Verschil)

Alles = Bruin.union(Groen)
print(Alles)
