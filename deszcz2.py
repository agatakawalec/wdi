import random
import os
import time

random.seed()
def deszczyk(szer,wys):
    for t in range(15):
        os.system('cls')
        for i in range(wys+1):
            a=random.randint(1,szer)
            print("O"*a+"X"+"O"*(szer-a-1))
        time.sleep(1)

    return "Koniec :)"

szerokosc=int(input("Podaj szerokosc\n"))
wysokosc=int(input("Podaj wysokosc\n"))
print(deszczyk(wysokosc, szerokosc))