baza="0123456789abcdefghijklmnoprstuvwxyz"
def dowolnytodec(wejscie,sys):
    global baza
    wynik=0
    for n in wejscie:
        wynik*=sys
        cyfra= baza.index(n)
        if int(n)>=int(sys):
            print("Niepoprawny system")
        wynik+=int(n)
    return wynik

def dectodowolny(wejscie,sys):
    global baza
    wynik=""
    while wejscie>0:
        wynik= (baza[wejscie%sys]) +wynik
        wejscie//=sys
    return wynik

x=int(input("Podaj podstawę systemu\n"))
print("Podaj liczbe w systemie",x,":")
wejscie=str(input())
a=dowolnytodec(wejscie,x)
print("Twoja liczba to:",a)
y=int(input("Podaj podstawę systemu\n"))
dec=int(input("Podaj liczbę w dziesiętnym\n"))
b=dectodowolny(dec,y)
print("Twoja liczba to:",b)