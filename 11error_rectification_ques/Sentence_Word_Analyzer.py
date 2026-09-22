#Take a sentence and examine every word.
#For each word:
#Print its length.
#Print "Short" if length ≤ 3.
#Print "Medium" if length is 4–6.
#Print "Long" if length > 6.
#At the end, print the number of short, medium, and long words.
#ques5
sentence = input("Enter a sentence: ")
short = 0
medium = 0
long = 0
for word in sentence.split():
    length = len(word)
    print(word, "Length:", length)
    if(length <= 3):
        print("Short")
        short += 1
    elif(length <= 6):
        print("Medium")
        medium += 1
    else:
        print("Long")
        long += 1
print("Short words:", short)
print("Medium words:", medium)
print("Long words:", long)