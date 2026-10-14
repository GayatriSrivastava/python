#Take a list of integers and a target number. If the target exists, print "Found". Otherwise, print "Not found" using for-else.
numbers=input("Enter integers separated by spaces: ").split()
target=input("Enter target number: ")
for i in numbers:
    if i==target:
        print("Found")
        break
else:
    print("Not found")