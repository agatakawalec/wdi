import time
import random
import sys
random.seed()
sys.setrecursionlimit(10000)

def tab_build(size):
    tab = []
    for i in range(size):
        tab.append(random.randint(0, 10000))
    return tab

def wybieranie(tablica):
    sorted=[]
    for i in range(len(tablica)):
        small=min(tablica)
        tablica.remove(small)
        sorted.append(small)
    return sorted

def wstawianie(tab):
    for index in range(1,len(tab)):
        value=tab[index]
        i=index-1
        while i>=0:
            if value<tab[i]:
                tab[i+1]=tab[i]
                tab[i]=value
                i-=1
            else:
                break
    return tab

def babelkowe(tab):
    for i in range(len(tab)-1,0,-1):
        for j in range(i):
            if tab[j]>tab[j+1]:
                tmp=tab[j]
                tab[j]=tab[j+1]
                tab[j+1]=tmp
    return tab


def quicksort(tab,start,end):
    if start>=end:
        return
    piwot=end
    j=start
    for i in range(start,end):
        if tab[i]<=tab[piwot]:
            tab[j],tab[i]=tab[i],tab[j]
            j+=1

    tab[j],tab[piwot]=tab[piwot],tab[j]
    piwot=j

    quicksort(tab,start,piwot-1)
    quicksort(tab,piwot+1,end)

    return tab

def mergesort(tab):
    if len(tab)<2:
        return tab

    middle=(len(tab))//2
    tmp=[]
    left=mergesort(tab[:middle])
    right=mergesort(tab[middle:])
    i,j=0,0
    lenleft=len(left)
    lenright=len(right)
    while i!=lenleft or j!=lenright:
        if i!=lenleft and (j==lenright or left[i]<right[j]):
            tmp.append(left[i])
            i+=1
        else:
            tmp.append(right[j])
            j+=1

    return tmp

def max_heap(tab,size,i):
    left_child=2*i+1
    right_child=2*i+2
    parent1=i #largest one
    if left_child<size and tab[left_child]>tab[parent1]:
        parent1=left_child
    if right_child<size and tab[right_child]>tab[parent1]:
        parent1=right_child
    if parent1!=i:
        tab[i],tab[parent1]=tab[parent1],tab[i]
        max_heap(tab,size,parent1)

def heap(tab):
    size=len(tab)
    for i in range((size//2),-1,-1):
        max_heap(tab,size,i)

def heapsort(tab):
    size=len(tab)
    heap(tab)
    for i in range(size-1,0,-1):
        tab[0],tab[i]=tab[i],tab[0]
        size-=1
        max_heap(tab,size,0)
    return tab


tab=tab_build(50)
print(tab)
print(wstawianie(tab))
print(babelkowe(tab))
print(quicksort(tab,0,len(tab)-1))
print(mergesort(tab))
print(heapsort(tab))
print(wybieranie(tab))