def convert(tempCelcius):
    tempFahrenheit = tempCelcius * 1.8 + 32
    return tempFahrenheit

def table():
    for tempCelcius in range(-30, 41, 10):
        tempFahrenheit = convert(tempCelcius)
        print("{1:5.1f} {0:5.1f}".format(tempFahrenheit, tempCelcius))

table()