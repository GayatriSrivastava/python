#Take a sentence.
#For every word:
#Vowel = 2 points.
#Consonant = 1 point.
#Digit = 3 points.
#Special character = 4 points.
#Calculate the score of every word and print the word with the highest score.
#Do not use max().
#ques3
sentence=input("enter a string:")
i=sentence.split()
vowel=0
consonant=0
digit=0
specialchar=0
for a in i:
    if(a in "AEIOUaeiou"):
        print("vowel")
        vowel+=2
    elif(a not in "AEIOUaeiou"and a.isalpha()):
        print("consonant")
    elif(a.isdigit()):
        print("digit")
        digit+=3
    else:
        print("specialcharacter")
        specialchar+=4
vowel_score=vowel
print(vowel_score)
consonant_score=consonant
print(consonant_score)
digit_score=digit
print(digit_score)
specialchar_score=specialchar
print(specialchar_score)
if(vowel_score>consonant_score and vowel_score>digit_score and vowel_score>specialchar_score):
    print("highest score is",vowel_score)
elif(consonant_score>vowel_score and consonant_score>digit_score and consonant_score>specialchar_score):
    print("highest score is",consonant_score)
elif(digit_score>vowel_score and digit_score>consonant_score and digit_score>specialchar_score):
    print("highest score is",digit_score)
else:
    print("highest score is",specialchar_score)
