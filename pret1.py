# ceny=[0,1,5,8,9,10,16,17,20,24,26]
# n=101
# a=0
# pierw=0
# drugi=0
#
# for i in range(11):
#     for j in range(11):
#         for k in range(n+1):
#             for l in range(n+1):
#                 if k*i+l*j==n:
#                     b=k*ceny[i]+l*ceny[j]
#                     if b>a:
#                         a=b
#                         pierw=i
#                         drugi=j
#                         licznik1=k
#                         licznik2=l
#                 else:
#                     pass
#
# print(a)
# print(licznik1,pierw)
# print(licznik2,drugi)

ceny=[0,1,5,8,9,10,16,17,20,24,26]

def jaktozrobic(n,max):
    global ceny
    primes=[0,1,2,3,5,7]
    a=0
    pierw=0
    drugi=0
    licznik1=0
    licznik2=0
    for i in range(max+1):
        for j in range(max+1):
            for k in range(n+1):
                for l in range(n+1):
                    if k*i+l*j==n:
                        b=k*ceny[i]+l*ceny[j]
                        if b>a:
                            a=b
                            pierw=i
                            drugi=j
                            licznik1=k
                            licznik2=l
                    else:
                        pass

    if pierw not in primes:
        oldp=pierw
        oldl=licznik1
        olda=a
        jaktozrobic(pierw*licznik1,pierw)
        if a>olda:
            print(licznik1, pierw, a)
        else:
            print(oldl, oldp, olda)
    else:
        print(licznik1, pierw, a)

    if drugi not in primes:
        oldd=drugi
        oldl2=licznik2
        olda=a
        jaktozrobic(drugi*licznik2,drugi)
        if a>olda:
            print(licznik2, drugi, a)
        else:
            print(oldl2, oldd, olda)
    else:
        print(licznik2, drugi, a)


    return "wlasnie tak!"



print(jaktozrobic(6,10))