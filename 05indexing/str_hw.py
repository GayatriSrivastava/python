#ques 1
name = "Gayatri"
city = 'Kanpur'
language = "Python"
message = 'I am learning Python programming.'
print(name)
print(city)
print(language)
print(message)
#ques 2
text = ""
print(text)
print(len(text))
print(type(text))
#ques 3
text = "Python Programming"
print(text)
print(len(text))
print(text[0])
print(text[-1])
print(text[2])
print(text[-2])
#ques 4
text = "Programming"
print(text[0])
print(text[1])
print(text[4])
print(text[10])
#ques 5
text = "Programming"
print(text[-1])
print(text[-2])
print(text[-3])
print(text[-11])
#ques 6
name = "Gayatri Srivastava"
print(name[0])
print(name[-1])
print(name[8])
#ques 7
text = "Python Programming"
print(text[0:6])
print(text[7:18])
print(text[:])
print(text[:5])
print(text[-5:])
#ques 8
text = "ABCDEFGHIJKL"
print(text[::2])
print(text[::3])
print(text[1:9:2])
print(text[::-1])
#ques 9
text = "Python Programming"
print(text[-5:])
print(text[-10:])
print(text[::-1])
#ques 10
text = "ABCDEFGHIJKL"
print(text[:3])
print(text[-3:])
print(text[::2])
print(text[::-1])
print(text[1:-1])
#ques 11
word = "Python"
sentence = "Python is easy."
sentence_spaces = "Python is very easy to learn."
print(len(word))
print(len(sentence))
print(len(sentence_spaces))
#ques 12
text = "Python Programming"
last_index = len(text) - 1
print(last_index)
print(text[last_index])
#ques 13
first_name = "Gayatri"
last_name = "Srivastava"
full_name = first_name + " " + last_name
print(full_name)
#ques 14
name = "Gayatri"
age = 18
city = "Kanpur"
language = "Python"
sentence = name + " is " + str(age) + " years old and lives in " + city + ". She is learning " + language + "."
print(sentence)
#ques 15
age = 18
print("Age: " + str(age))
#ques 16
symbol = "*"
print(symbol * 3)
print(symbol * 5)
print(symbol * 10)
#ques 17
print("*" * 10)
#ques 18
text = "python programming language"
print(text.upper())
print(text.lower())
print(text.capitalize())
print(text.title())
print(text.swapcase())
#ques 19
text1 = "Python"
text2 = "python"
print(text1 == text2)
print(text1.lower() == text2.lower())
#ques 20
text = "Python is a programming language"
print("Python" in text)
print("programming" in text)
print("Java" in text)
print("language" in text)
#ques 21
text = "Python is a programming language"
print(text.find("Python"))
print(text.find("programming"))
print(text.find("language"))
print(text.find("Java"))
#ques 22
text = "Python is a programming language"
print(text.index("Python"))
print(text.index("programming"))
print(text.index("language"))
# print(text.index("Java"))
#ques 23
text = "banana"
print(text.count("a"))
print(text.count("n"))
print(text.count("b"))
#ques 24
filename = "student_notes.pdf"
print(filename.startswith("student"))
print(filename.endswith(".pdf"))
print(filename.endswith(".txt"))
#ques 25
text = "I am learning Java"
new_text = text.replace("Java", "Python")
print(new_text)
#ques 26
text = "apple apple apple"
new_text = text.replace("apple", "mango")
print(new_text)
#ques 27
text = "apple apple apple"
new_text = text.replace("apple", "mango", 1)
print(new_text)
#ques 28
text = "Python"
text.upper()
print(text)
text = text.upper()
print(text)
#ques 29
text = "   Python Programming   "
print(text.strip())
print(text.lstrip())
print(text.rstrip())
#ques 30
name = input("Enter your name: ")
cleaned_name = name.strip()
print(cleaned_name)
#ques 31
text = "Python is easy to learn"
words = text.split()
print(words)
#ques 32
text = "apple,banana,mango,orange"
fruits = text.split(",")
print(fruits)
#ques 33
words = ["Python", "is", "easy"]
sentence = " ".join(words)
print(sentence)
#ques 34
words = ["Python", "is", "easy"]
print("-".join(words))
print("/".join(words))
#ques 35
name = "Gayatri"
age = 18
city = "Kanpur"
sentence = f"My name is {name}, I am {age} years old, and I live in {city}."
print(sentence)
#ques 36
a = 10
b = 20
print(f"The sum is {a + b}")
#ques 37
text = "Python"
# print(text[20])
text = "Python"
# text[0] = "J"
text = "J" + text[1:]
print(text)
age = 20
print("Age: " + str(age))
text = "Python"
# print(text.index("Java"))
print(text.find("Java"))
#ques 38
name = input("Enter your full name: ")
cleaned_name = name.strip()
print("Original input:", name)
print("Cleaned name:", cleaned_name)
print("Uppercase:", cleaned_name.upper())
print("Lowercase:", cleaned_name.lower())
print("Title case:", cleaned_name.title())
print("Length:", len(cleaned_name))
print("First character:", cleaned_name[0])
print("Last character:", cleaned_name[-1])
character = input("Enter a character to search: ")
print("Character exists:", character in cleaned_name)
#ques 39
sentence = input("Enter a sentence: ")
print("Original sentence:", sentence)
print("Number of characters:", len(sentence))
print("Number of words:", len(sentence.split()))
print("First character:", sentence[0])
print("Last character:", sentence[-1])
print("Uppercase:", sentence.upper())
print("Lowercase:", sentence.lower())
print("Title case:", sentence.title())
print("Python exists:", "Python" in sentence)
character = input("Enter a character to count: ")
print("Number of times it occurs:", sentence.count(character))
#ques 40
first_name = input("Enter first name: ").strip()
last_name = input("Enter last name: ").strip()
city = input("Enter city: ").strip()
course = input("Enter course: ").strip()
age = int(input("Enter age: "))
full_name = first_name + " " + last_name
print("Full name:", full_name)
print("Title case:", full_name.title())
print("Uppercase:", full_name.upper())
print("Lowercase:", full_name.lower())
print("Length:", len(full_name))
print("First character:", full_name[0])
print("Last character:", full_name[-1])
print("City:", city)
print("Course:", course)
print(f"Age: {age}")
print("Course contains Python:", "Python" in course)
new_course = course.replace("Python", "Java", 1)
print("Updated course:", new_course)
print("Number of words in course:", len(course.split()))