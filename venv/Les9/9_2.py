while True:
    string = input("Geef een string van vier letters: ")
    if len(string) != 4:
        continue
    else:
        break
print("Inlezen van correcte string: " + string + " is geslaagd")