def silniaiter(n):
    wynik=1
    if n==1 or n==0:
        wynik=1
    else:
        for i in range(1,n+1):
            wynik*=i

    return wynik

def silniarek(n):
    wynik=1
    if n==1 or n==0:
        wynik=1
    else:
        wynik*=silniarek(n-1)*n

    return wynik

def fiboiter(n):
    wynik=1
    if n==0:
        wynik=0
    elif n==1:
        wynik=1
    else:
        a=0
        b=1
        for i in range(2,n+1):
            wynik=a+b
            a=b
            b=wynik

    return wynik

def fiborek(n):
    if n==0:
        wynik=0
    elif n==1:
        wynik=1
    else:
        wynik=fiborek(n-2)+fiborek(n-1)


    return wynik

print(silniaiter(5))
print(silniarek(5))
print(fiboiter(8))
print(fiborek(8))

