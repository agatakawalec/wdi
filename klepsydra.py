# n=7
# print("*"*n)
# for i in range(n-2,0,-2):
#     print(" " * ((n - i) // 2) + "*" * i)
# for j in range(3,n-1,2):
#     print(" "*((n-j)//2)+"*"*j)
# print("*"*n)

# n=3
# if n==1:
#     print("*")
# else:
#     print("*")
#     for q in range(1,n+1):
#         print("*"*(2*q+1))
#         for i in range(2*q-1,0,-2):
#             print(" " * ((2*q+1-i) // 2) + "*" * i)
#         for j in range(3,2*q,2):
#             print(" "*((2*q+1-j)//2)+"*"*j)
#         print("*"*(2*q+1))

n=5
if n==1:
    print("*")
else:
    print("*")
    for q in range(1,n+1):
        print("*"*(2*q+1))
        for i in range(2*q-1,1,-2):
            print(" "*((2*q+1-i)//2)+"*"+" "*(i-2)+"*")
        print(" "*q +"*")
        for j in range(3,2*q,2):
            print(" "*((2*q+1-j)//2)+"*" +" "*(j-2)+ "*")
        print("*"*(2*q+1))