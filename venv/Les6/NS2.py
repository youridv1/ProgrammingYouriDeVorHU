def standaardprijs(afstandKM):
    if afstandKM > 50:
        res = 15 + afstandKM*0.6
    else:
        res = afstandKM*0.8
    if res < 0:
        res = 0
    return res


def ritprijs(leeftijd, weekendrit, afstandKM):
    res1 = standaardprijs(afstandKM)
    if weekendrit == False and leeftijd < 12 or leeftijd >= 65 and weekendrit == False:
        res0 = res1 * 0.70
    else:
        if weekendrit == True and leeftijd < 12 or leeftijd >= 65 and weekendrit == True:
            res0 = res1 * 0.65
        else:
            if weekendrit == True and leeftijd >= 12 and leeftijd < 65:
                res0 = res1 * 0.60
            else:
                res0 = res1

    print(res0)

ritprijs(int(input("Geef je leeftijd: ")), bool(input("Is dit een weekendrit? (True/False) ")), int(input("Hoe lang is de reis? ")))
