#Take a word and count how many characters are not vowels. Use continue to skip vowels.
word=input("Enter a word: ")
count=0
for i in word:
    if i.lower() in "aeiou":
        continue
    count+=1
print(count)