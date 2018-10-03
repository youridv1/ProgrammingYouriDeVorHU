def seizoen(maand):
    maand = int(maand)
    if maand >= 3 and maand <= 5:
        return 'lente'
    elif maand >= 6 and maand <= 8:
        return 'zomer'
    elif maand >= 9 and maand <= 11:
        return 'herfst'
    else:
        return 'winter'

print(seizoen(12))