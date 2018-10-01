def convert(tempCelcius):
    tempFahrenheit = tempCelcius * 1.8 + 32
    return tempFahrenheit

def table():
    print("{1:>3} {0:>5}".format("C", "F"))
    for tempCelcius in range(-30, 41, 10):
        tempFahrenheit = convert(tempCelcius)
        print("{0:5.1f} {1:5.1f}".format(tempFahrenheit, tempCelcius))

table()