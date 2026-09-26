n=int(input("enter number"))
for i in range(0,n+1,2):
    for j in range(i+1):
        if(j%2==0):
            print(j,end=" ")
    print()