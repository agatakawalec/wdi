def pascal(n):
    if n==1:
        print("1")
        return [1]
    elif n==2:
        pascal(n-1)
        print("1 1")
        return [1,1]
    else:
        last=pascal(n-1)
        new=[1,1]
        for i in range(1,len(last)):
            new.insert(i,last[i]+last[i-1])

        for j in new:
            print(j,end=" ")
            
    print()
    return new

print(pascal(5))

