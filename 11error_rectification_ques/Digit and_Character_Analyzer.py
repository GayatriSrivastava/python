#Take a string containing letters, digits, spaces, and special characters.
#Using a for loop:
#Count uppercase letters.
#Count lowercase letters.
#Count digits.
#Count spaces.
#Count special characters.
#Print which category has the highest count.
#If two or more categories have the same highest count, print "Tie".
str=input("enter a string:")
uppercase=0
lowercase=0
digits=0
spaces=0
special=0

for ch in str:
    if ch.isupper():
        uppercase+=1
    elif ch.islower():
        lowercase+=1
    elif ch.isdigit():
        digits+=1
    elif ch==" ":
        spaces+=1
    else:
        special+=1

print("uppercase:",uppercase)
print("lowercase:",lowercase)
print("digit:",digits)
print("spaces:",spaces)
print("special:",special)

if uppercase > lowercase and uppercase > digits and uppercase > spaces and uppercase > special:
    print("Uppercase has the highest count")

elif lowercase > uppercase and lowercase > digits and lowercase > spaces and lowercase > special:
    print("Lowercase has the highest count")

elif digits > uppercase and digits > lowercase and digits > spaces and digits > special:
    print("Digits have the highest count")

elif spaces > uppercase and spaces > lowercase and spaces > digits and spaces > special:
    print("Spaces have the highest count")

elif special > uppercase and special > lowercase and special > digits and special > spaces:
    print("Special characters have the highest count")

else:
    print("Tie")