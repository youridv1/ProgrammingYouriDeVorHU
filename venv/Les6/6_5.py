def kwadraten_som(grondgetallen):
    res = 0
    for i in grondgetallen:
        if i>0:
            res = res + i**2
    return res



print(kwadraten_som([4, 5, 3, -81]))





