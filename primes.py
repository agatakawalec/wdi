import math
def primes(tab):
    n=0
    while n <len(tab)-1:
        n+=1
        for i in range(2,int(math.sqrt(tab[n])+1)):
            if tab[n]%i==0 and i!=tab[n]:
                del tab[n]
                n-=1
                break
    return tab

a=[5,8,6,97]
print(primes(a))
