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

#ritprijs(int(input("Geef je leeftijd: ")), bool(input("Is dit een weekendrit? (True/False) ")), int(input("Hoe lang is de reis? "))) #voor wanneer je met input wil werken
#de 24 mogelijke randvoorwaarden
test_1 = ritprijs(11, True, 30)
test_2 = ritprijs(12, True, 30)
test_3 = ritprijs(64, True, 30)
test_4 = ritprijs(65, True, 30)
test_5 = ritprijs(11, False, 30)
test_6 = ritprijs(12, False, 30)
test_7 = ritprijs(64, False, 30)
test_8 = ritprijs(65, False, 30)
test_9 = ritprijs(11, True, 60)
test_10 = ritprijs(12, True, 60)
test_11 = ritprijs(64, True, 60)
test_12 = ritprijs(65, True, 60)
test_13 = ritprijs(11, False, 60)
test_14 = ritprijs(12, False, 60)
test_15 = ritprijs(64, False, 60)
test_16 = ritprijs(65, False, 60)
test_17 = ritprijs(11, True, -30)
test_18 = ritprijs(12, True, -30)
test_19 = ritprijs(64, True, -30)
test_20 = ritprijs(65, True, -30)
test_21 = ritprijs(11, True, -30)
test_22 = ritprijs(12, False, -30)
test_23 = ritprijs(64, False, -30)
test_24 = ritprijs(65, False, -30)


