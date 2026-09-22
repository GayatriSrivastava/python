for i in range(4):
    for j in range (4):
        print("*") #by default print ka behaviour hai ki next print ka output next line pe jayega


#for i in range(4):
    #for j in range (4):
     #   print("*",end="")#nayi line se start nhi hoga

for i in range(5):
    for j in range(i+1):
        print("*",end="")
    print("")

for i in range(5):
    for j in range(5-i):
        print("*",end="")
    print("")


n = int(input("Enter your number: "))
for i in range(1, n + 1):
    for j in range(i):
        print(j+ 1, end="")
    print("")