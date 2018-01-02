n=3
# for i in range(2,n+1):
#     for j in range(i+1):
#         print("*"*j)

# for i in range(n):
#     for j in range(i):
#         print(" "*(n-j)+"*"*j+"*"+"*"*j)
#         print(" "*(n-j)+"o"**+" "*(j-1)+"o"+" "*(j-1)+"o")

# print(" "*(n)+"X")
# for i in range(0,n+1):
#     print(" "*(n-i)+"*"*i+"*"+"*"*i+" "*(n-i))
#     if i>=1:
#         if i%2!=0:
#             print(" "*(n-i)+("o"+" ")*(i+1)+" "*(n-1))
#         else:
#             print(" "*(n-i)+("o"+" ")*(i)+"o")

# p=7
# for i in range(3,p+1,2):
#     print("x"*i)
#     for j in range(1,i-1):
#         print("x"+" "*(i-2)+("x"))
#     print("x"*i)

# import random
# import time
# import os
# random.seed()
#
# w=7
# s=10
# for j in range(1,5):
#     os.system('cls')
#     for i in range(1,n+1):
#         r=random.randint(1,s)
#         print("o"*(r-1)+"x"+"o"*(s-r))
#     print("\n")
#     time.sleep(1)

if n==1:
    print("*")
else:
    for k in range(1,n+1):
        print("*"*(2*k+1))
        for i in range(1,n):
            for j in range(1,n-1):
                print(" "*j+"*"+" "*(2*n-5))