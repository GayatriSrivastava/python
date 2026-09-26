n=int(input("enter number:"))
for i in range(0,n+1):
    for j in range(1,i+1):
        if (i>=j):
            print(chr(64+i),end=" ")
    print()
