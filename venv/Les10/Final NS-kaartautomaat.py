def inlezen_beginstation(stations):
    station = input('Wat is je beginstation? ')
    if station in stations:
        return station
    else:
        print('Deze trein komt niet langs ' + str(station))
        inlezen_beginstation(stations)

def inlezen_eindstation(stations, beginstation):
    station = input('Wat is je eindstation? ')
    if station in stations and stations.index(station) > stations.index(beginstation):
      return station
    else:
        print('Deze trein komt vanaf ' + str(beginstation + ' niet langs ' + str(station)))
        inlezen_eindstation()

def omroepen_reis(stations, beginstation, eindstation):
    afstand = str(stations.index(eindstation) - stations.index(beginstation))
    prijs = int(afstand) * 5
    prijs = str(prijs)
    slice = stations[1 + stations.index(beginstation):stations.index(eindstation)]
    print('Het beginstation ' + str(beginstation + 'is het ' + str(1 + stations.index(beginstation))) + 'e station in het traject.\n'
        'Het eindstation ' + str(eindstation + 'is het ' + str(1 + stations.index(eindstation))) + 'e station in het traject.\n'
        'De afstand bedraagt ' + afstand + ' station(s)\n'
        'De prijs van het kaartje is ' + str(prijs) + ' euro.\n'
        'U komt onderweg langs de station(s) ' + str(slice).strip('[]'))

stations = ['Schagen', 'Heerhugowaard', 'Alkmaar', 'Castricum', 'Zaandam', 'Amsterdam Sloterdijk', 'Amsterdam Centraal', 'Amsterdam Amstel', 'Utrecht Centraal', "'s-Hertogenbosch", 'Eindhoven', 'Weert', 'Roermond', 'Sittard', 'Maastricht']
beginstation = inlezen_beginstation(stations)
eindstation = inlezen_eindstation(stations, beginstation)
omroepen_reis(stations, beginstation, eindstation)