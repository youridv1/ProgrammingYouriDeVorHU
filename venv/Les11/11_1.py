aantalstring = input('Hoeveel mensen gaan er mee? ')
aantalint = int(aantalstring)
if aantalint > 0:
    try:
        prijspp = 4356 / aantalint
        print(prijspp)
    except ZeroDivisionError:
        print('Delen door nul gaat niet!')
    except ValueError:
        print('Gebruik de getallen 0-9!')
    except:
        print('Onjuiste invoer!')
else:
    print('Negatieve getallen zijn niet toegestaan!')
