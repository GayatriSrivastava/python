n =5
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if j == 1 or i == n or j == n:
            print("* ", end="")#we can also write it as print("*"+" ",end="")
        elif (i%2!=0 and j%2!=0 and n!=1 and i!=1):
            print("* ",end="")
        else:                                                                                                                                                                                                                   
            print("  ", end="")
    print()

