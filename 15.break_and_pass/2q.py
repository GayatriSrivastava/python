#Take a string and a target character. Scan the string from left to right. Print each character as it is checked. Stop immediately after finding the target.
#If the target does not appear, check the entire string.
str=input("enter a string")
character=input("enter the character you want to match in string")
for i in str:
    if i==character:
        print(character)
        break
