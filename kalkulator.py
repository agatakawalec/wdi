print("Podaj działanie:\n")
dzialanie=str(input())
if dzialanie.find('+') != -1:
    x,y= dzialanie.split('+')
    dodawanie=int(x)+int(y)
    print(dodawanie)
elif dzialanie.find('-') != -1:
    x,y= dzialanie.split('-')
    odejmowanie=int(x)-int(y)
    print(odejmowanie)
elif dzialanie.find('**') != -1:
    x,y= dzialanie.split('**')
    potegowanie=int(x)**int(y)
    print(potegowanie)
elif dzialanie.find('*') != -1:
    x,y= dzialanie.split('*')
    mnozenie=int(x)*int(y)
    print(mnozenie)
elif dzialanie.find('/') !=-1:
    x,y=dzialanie.split('/')
    if y==0:
        print("Nie dzielimy przez 0")
    else:
        dzielenie=int(x)/int(y)
        print(dzielenie)

else:
    print("Niewspierane działanie")