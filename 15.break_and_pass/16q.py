#Read integers from a list in order
numbers=list(map(int,input("Enter numbers separated by spaces: ").split()))
for i in numbers:
    if i==-1:
        break
    if i==0:
        continue
    print(i)
else:
    print("All values processed")