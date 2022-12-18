n=int(input("enter any num:"))
for i in range(n):
    for j in range(0,n+i-n):
        print(" ",end=" ")
    for k in range(n+i-n,n):
              print("*",end=" ")
    print()
