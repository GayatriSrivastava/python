str = input("Enter a string: ")
i = 0
j = len(str) - 1
flag = True
while i < j:
    if str[i] == str[j]:
        flag = True
    else:
        flag = False
        break
    i += 1
    j -= 1
if flag == True:
    print("Palindrome")
else:
    print("Not Palindrome")

#or
str = input("Enter a string: ")
i = 0
j = len(str) - 1
flag = True
while i < j:
    if str[i] == str[j]:
        i += 1
        j -= 1
    else:
        flag = False
        i==j #to break the loop
if flag:
    print("Palindrome")
else:
    print("Not Palindrome")