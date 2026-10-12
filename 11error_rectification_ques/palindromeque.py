#check whether the given string is palindrome or not

s=input("Enter a string: ")

i=len(s)-1
rev=""

while(i>=0):
    rev=rev+s[i]
    print(rev)
    i-=1

print(rev)
if(s==rev):
    print("Palindrome")
else:
    print("Not a palindrome")