#check whether the given string is palindrome or not.
str=input("enter the string").strip()
sum=""
length=len(str)
for element in range(length-1,-1,-1):
    sum=sum+str[element]
print(sum)
if (sum==str):
    print("it is palindrome")
else:
    print("not palindrome")
    