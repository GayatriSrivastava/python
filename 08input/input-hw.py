#ques 1
name = input("Enter your name: ")
print(name)

#ques 2
city = input("Enter your city: ")
print(f"Your city is {city}")

#ques 3
name = input("Enter your name: ")
age = input("Enter your age: ")
print(name)
print(age)

#ques 4
# input() returns a string (str) by default

#ques 5
value = input("Enter a value: ")
print(type(value))

#ques 6
first_name = input("Enter first name: ")
last_name = input("Enter last name: ")
print(first_name, last_name)

#ques 7
name = input("Enter your name: ")
city = input("Enter your city: ")
college = input("Enter your college: ")
print(name)
print(city)
print(college)

#ques 8
name1, name2 = input("Enter two names: ").split()
print(name1)
print(name2)

#ques 9
name1, name2 = input().split()
# If input is: Python Programming
# name1 = "Python"
# name2 = "Programming"

#ques 10
word1, word2, word3 = input("Enter three words: ").split()
print(word1)
print(word2)
print(word3)

#ques 11
num = int("25")
print(num)

#ques 12
num = float("25.5")
print(num)

#ques 13
num = 100
text = str(num)
print(text)

#ques 14
num = int(input("Enter an integer: "))
print(type(num))

#ques 15
num = float(input("Enter a floating-point number: "))
print(type(num))

#ques 16
a = input()
b = input()
print(a + b)
# input() returns strings, so + performs string concatenation

#ques 17
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print(a + b)

#ques 18
name = "Rahul"
age = 20
print(f"My name is {name} and I am {age} years old.")

#ques 19
a = 10
b = 20
print(f"Sum = {a + b}")

#ques 20
name = input("Enter your name: ")
age = int(input("Enter your age: "))
print(f"My name is {name} and I am {age} years old.")

#ques 21
price = float(input("Enter price: "))
print(f"{price:.2f}")

#ques 22
# :.2f displays a floating-point number with exactly 2 decimal places

#ques 23
product = input("Enter product name: ")
price = float(input("Enter price: "))
quantity = int(input("Enter quantity: "))
print(f"Product: {product}")
print(f"Price: {price}")
print(f"Quantity: {quantity}")

#ques 24
print("A", "B", "C")
# Output: A B C

#ques 25
print("2026", "08", "19", sep="-")

#ques 26
print("Hello", end=" ")
print("World")

#ques 27
first = int(input("Enter first number: "))
second = int(input("Enter second number: "))
sum = first + second
print(f"First number: {first}")
print(f"Second number: {second}")
print(f"Sum: {sum}")

#ques 28
price = float(input("Enter price: "))
quantity = int(input("Enter quantity: "))
total = price * quantity
print(f"Price: {price}")
print(f"Quantity: {quantity}")
print(f"Total: {total}")

#ques 29
name = input("Enter student name: ")
age = int(input("Enter student age: "))
marks = float(input("Enter marks: "))
print(f"Name: {name}, Age: {age}, Marks: {marks}")

#ques 30
name = input("Enter student name: ")
age = int(input("Enter student age: "))
height = float(input("Enter student height: "))
city = input("Enter city: ")
print(f"Name: {name}")
print(f"Age: {age}")
print(f"Height: {height:.2f}")
print(f"City: {city}")