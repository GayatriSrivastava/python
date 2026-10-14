for i in range(1,6):
    for j in range(1,6):
        if(j>i):
            print(" ",end="")
        else:
            if(j==1):
                print("A ",end="")
            elif(j==2):
                print("B ",end="")
            elif(j==3):
                print("C ",end="")
            elif(j==4):
                print("D ",end="")
            else:
                print("E ",end="")
    print()
#or  can do it like 
n=int(input("enter number:"))
for i in range(n+1):
    for j in range(i+1):
            print(chr(65+j),end=" ")
    print()

