#Search for a target number in a list
numbers=list(map(int,input("Enter numbers separated by spaces: ").split()))
target=int(input("Enter target number: "))
for i in numbers:
    if i<0:
        continue
    if i==target:
        print("Target found")
        break
else:
    print("Target not found")