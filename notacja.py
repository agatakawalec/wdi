class Node:
    def __init__(self,data):
        self.data=data
        self.prev=None

class Stos:
    def __init__(self):
        self.top=None
        self.size=0

    def push(self,data):
        n=self.top
        new=Node(data)
        self.top=new
        new.prev=n
        self.size+=1

    def pop(self):
        n=self.top.data
        prev=self.top.prev
        self.top=prev
        self.size-=1
        return n

    def isEmpty(self):
        if self.top==None:
            return True
        else:
            return False


stos=Stos()
wyrazenie=str(input("Podaj wyrażenie"))

tmp=''

for i in range(len(wyrazenie)):
    if wyrazenie[i].isdigit():
        tmp+=wyrazenie[i]

    elif wyrazenie[i]==' ':
        stos.push(int(tmp))
        tmp=""

    elif wyrazenie[i]=='+':
        a=stos.pop()
        b=stos.pop()
        stos.push(a+b)
    elif wyrazenie[i]=='-':
        a=stos.pop()
        b=stos.pop()
        stos.push(a-b)
    elif wyrazenie[i]=='*':
        a = stos.pop()
        b = stos.pop()
        stos.push(a*b)
    elif wyrazenie[i]=='/':
        a = stos.pop()
        b = stos.pop()
        stos.push(a/b)

print(stos.pop())





