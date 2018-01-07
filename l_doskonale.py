def doskonale(liczba):
    tab=[]
    dzielniki=[]
    for i in range(1,liczba//2+1):
        tab.append(i)

    for c in tab:
        if liczba%c==0:
            dzielniki.append(c)
        else:
            pass

    print(tab)
    print(dzielniki)
    suma=0
    for i in dzielniki:
        suma+=i

    print(suma)
    if suma==liczba:
        print("WOOW TA LICZBA JEST DOSKONAŁA")
    else:
        print("Kurka, nie jest doskonała :(")

print(doskonale(20))