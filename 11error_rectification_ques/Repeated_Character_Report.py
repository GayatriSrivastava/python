#Take a string.
#For every character, determine how many times it appears in the string without using count().
#Print only characters that appear more than once.
#Also classify them:
#2 occurrences → "Duplicate"
#3–4 occurrences → "Repeated"
#More than 4 → "Highly Repeated"
#ques7
text = input("Enter a string: ")
seen = ""
for ch in text:
    if ch not in seen:
        frequency = 0
        for x in text:
            if ch == x:
                frequency += 1
        if frequency > 1:
            print(ch, "=", frequency)
            if frequency == 2:
                print("Duplicate")
            elif frequency <= 4:
                print("Repeated")
            else:
                print("Highly Repeated")
        seen += ch