import datetime
vandaag = datetime.datetime.today()
s = vandaag.strftime("%a %d %b %Y")
t = vandaag.strftime("%I:%M:%S")

infile = open('hardlopers.txt', 'a')
naam = input("naam: ")
naam = naam.strip()
naam = naam.lower()
naam = naam.capitalize() #zodat wat voor onzin de user ook maar invoert, het netjes in lowercase is en begint met een hoofdletter
datum = s
tijd = t
infile.write(str(s) + ", " + str(t) + ", " + naam + "\n")
infile.close()