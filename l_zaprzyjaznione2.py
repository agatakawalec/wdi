def dzielniki(liczba):
    dzielniki=[]
    for i in range(1,liczba//2+1):
        if liczba%i==0:
            dzielniki.append(i)
    return dzielniki

def zliczanie(liczba):
    dzielnikii=dzielniki(liczba)
    suma=0
    for e in dzielnikii:
        suma+=e
    return suma

def przyjazn(liczba):
    for i in range(1,liczba+1):
        suma_d=zliczanie(i)
        suma2=zliczanie(suma_d)
        if i==suma2 and suma_d!=i:
            print("liczby zaprzyjaznione to:",i,suma_d)
        else:
            i+=1

    return 0
print(dzielniki(20))
print(zliczanie(20))
print(przyjazn(300))