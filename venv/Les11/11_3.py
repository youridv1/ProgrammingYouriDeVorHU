import csv
with open('scores.csv', 'r') as scores:
    reader = csv.reader(scores, delimiter=';')
    score = 0
    score = int(score)
    naam = str
    datum = str
    for row in reader:
        temp = int(row[2])
        if temp > score:
            naam, datum, score = row[0], row[1], int(row[2])
    print('De hoogste score is: ', score, ' op ', datum, ' behaald door ', naam)

