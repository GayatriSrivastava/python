#Given a string, print the first character that repeats later. If no character repeats, print "No repeated character".
s=input("Enter a string: ")
for i in range(len(s)):
    if s[i] in s[i+1:]:
        print(s[i])
        break
else:
    print("No repeated character")