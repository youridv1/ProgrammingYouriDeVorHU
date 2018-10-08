def ticker():
    filename = open("tickets.txt")
    temp = []
    tickers = {}
    lines = filename.readlines()
    for line in lines:
        temp = line.split(sep = ':')
        temp[1] = temp[1].strip()
        tickers[temp[0]] = temp[1]
    return tickers

def printer():
    tickers = ticker()
    keuze = input("1. Ik weet de bedrijfsnaam.\n"
                  "2. Ik weet het tickersymbol.\n"
                  "Voer uw keuze in: ")
    if int(keuze) == 1:
        name = input("Enter Company name: ")
        print(tickers[name])
    elif int(keuze) == 2:
        tick = input("Enter Ticker symbol: ")
        for key, value in tickers.items():
            if value == tick:
                print(key)

printer()

