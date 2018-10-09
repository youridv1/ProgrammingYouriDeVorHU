
import random
throws = 0

def monopolyworp(throws):
    throws += 1
    t1 = random.randrange(1, 7)
    t2 = random.randrange(1, 7)
    if t1 == t2:
        if throws >= 3:
            print('Naar de gevangenis')
        else:
            print('Gelijk')
            monopolyworp(throws)
    else:
        print('Niet gelijk')


monopolyworp(throws)