#Find the first number divisible by both 4 and 6
numbers=list(map(int,input("Enter numbers separated by spaces: ").split()))
for i in numbers:
    if i<0:
        continue
    if i%4==0 and i%6==0:
        print(i)
        break
else:
    print("No matching number exists")