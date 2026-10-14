n=int(input("enter number:"))
for i in range(1,n+1,2):
    for j in range(1,i+1):
        if(j%2!=0):
          print(j,end=" ") 
    print()

    #or
n=int(input("enter number:"))
for i in range(n+1):
    for j in range(i+1):
        print(j*2-1,end="")
    print()


