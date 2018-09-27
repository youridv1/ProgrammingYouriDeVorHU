def check_number(newpassword):
    numbers = 0
    number_list = "1 2 3 4 5 6 7 8 9 0"
    for char in newpassword:
        if char in number_list:
            numbers += 1
    if numbers > 0:
        return True
    else:
        return False


def new_password(oldpassword, newpassword):
    if oldpassword != newpassword and len(oldpassword)>5 and check_number(newpassword):
        print(True)
    else:
        print(False)

new_password("wachtwoord1", "wachtwoord2")