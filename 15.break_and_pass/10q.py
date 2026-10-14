#Check Whether a Character Exists
s=input("Enter a string: ")
target=input("Enter target character: ")
for i in s:
    if i==target:
        print("Character exists")
        break
else:
    print("Character missing")