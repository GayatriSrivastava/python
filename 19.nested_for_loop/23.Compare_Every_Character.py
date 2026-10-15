str=input("enter a string containing two characters:")
for i in str:
    for j in str:
        if i==j:
            print(i,j,"same")
        else:
            print(i,j,"different")
