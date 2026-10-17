str=input("enter first string: ")
ch=input("enter second string: ")
count=0
for i in str:
    for j in ch:
        if(i==j):
            count+=1
print(count)
print()