def check_number(b):
    numbers = 0
    number_list = "1 2 3 4 5 6 7 8 9 0"
    for char in b:
        if char in number_list:
            numbers += 1
    if numbers > 0:
        return True
    else:
        return False


def new_password(a, b):
    if a != b and len(a)>5 and check_number(b):
        print(True)
    else:
        print(False)

new_password("wachtwoord1", "wachtwoord2")