#Take a sentence and a target word. Check the words from left to right. Print "Found" and stop when the target word is found. If the target is absent, print "Not found".
sentence=input("Enter a sentence: ").split()
target=input("Enter target word: ")
for i in sentence:
    if i==target:
        print("Found")
        break
else:
    print("Not found")