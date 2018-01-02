import time
import random
import os

random.seed()
tab=[None] * 10
for t in range(15):
    os.system('cls')
    for i in range(10):
        if(i==0):
            losowana = random.randrange(7)
            tab.insert(0,losowana)

        if(tab[i]==None):
            print('o ' *7)
        else:
            a=tab[i]
            print('o '*(a) + 'x ' + 'o ' *(6-a))
    time.sleep(0.5)
