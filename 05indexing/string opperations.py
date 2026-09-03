# Task 1

name = "Gayatri"
city = 'Ahmedabad'
language = "Python"
message = 'I am learning Python programming.'
print(name)
print(city)
print(language)
print(message)

# Task 2

text = ""
print(text)
print(len(text))
print(type(text))

# Task 3

text = "Python Programming"
print(text)
print(len(text))
print(text[0])
print(text[-1])
print(text[2])
print(text[-2])

# Task 4

text = "Programming"
print(text[0])
print(text[1])
print(text[4])
print(text[-1])

# Task 5

text = "Programming"
print(text[-1])
print(text[-2])
print(text[-3])
print(text[-11])

# Task 6

name = "Gayatri Srivastava"
print(name[0])
print(name[-1])
print(name[8])

# Task 7

text = "Python Programming"
print(text[0:6])
print(text[7:18])
print(text[:])
print(text[:5])
print(text[-5:])

# Task 8

text = "ABCDEFGHIJKL"
print(text[::2])
print(text[::3])
print(text[1:9:2])
print(text[::-1])

# Task 9

text = "Python Programming"
print(text[-5:])
print(text[-10:])
print(text[::-1])

# Task 10

text = "Programming"
print(text[:3])
print(text[-3:])
print(text[::2])
print(text[::-1])
print(text[1:-1])

# Task 11

word = "Python"
sentence = "I am learning Python."
sentence_spaces = "I am learning Python programming."
print(len(word))
print(len(sentence))
print(len(sentence_spaces))

# Task 12

text = "Python Programming"
last_index = len(text) - 1
print(last_index)
print(text[last_index])

# Task 13

first_name = "Gayatri"
last_name = "Srivastava"
full_name = first_name + " " + last_name
print(full_name)

# Task 14

name = "Gayatri"
age = 18
city = "Ahmedabad"
language = "Python"
sentence = "My name is " + name + ", I am " + str(age) + " years old, I live in " + city + " and I am learning " + language + "."
print(sentence)

# Task 15

text = "My age is "
age = 18
print(text + str(age))

# Task 16

symbol = "*"
print(symbol * 3)
print(symbol * 5)
print(symbol * 10)

# Task 17

symbol = "*"
print(symbol * 10)

# Task 18

text = "python programming language"
print(text.upper())
print(text.lower())
print(text.capitalize())
print(text.title())
print(text.swapcase())

# Task 19

text1 = "Python"
text2 = "python"
print(text1 == text2)
print(text1.lower() == text2.lower())

# Task 20

text = "Python is a programming language"
print("Python" in text)
print("programming" in text)
print("Java" in text)
print("language" in text)

# Task 21

text = "Python is a programming language"
print(text.find("Python"))
print(text.find("programming"))
print(text.find("language"))
print(text.find("Java"))

# Task 22

text = "Python is a programming language"
print(text.index("Python"))
print(text.index("programming"))
print(text.index("language"))
try:
print(text.index("Java"))
except ValueError:
print("Java not found")

# Task 23

text = "banana"
print(text.count("a"))
print(text.count("n"))
print(text.count("b"))

# Task 24

filename = "student_notes.pdf"
print(filename.startswith("student"))
print(filename.endswith(".pdf"))
print(filename.endswith(".txt"))
