n=int(input("enter number: "))
for i in range(1,n+1):
    for j in range(1,n+1):
        if(j%i==0):
            print(j,end=" ")
    print()