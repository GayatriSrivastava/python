a = 20
b = 6
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Floor division:", a // b)
print("Modulus:", a % b)
print("Exponentiation:", a ** b)

number1 = 10
number2 = 2.5

result = number1 + number2
print("Addition:", result, type(result))

result = number1 - number2
print("Subtraction:", result, type(result))

result = number1 * number2
print("Multiplication:", result, type(result))

result = number1 / number2
print("Division:", result, type(result))

result = number1 // number2
print("Floor division:", result, type(result))

result = number1 % number2
print("Modulus:", result, type(result))

result = number1 ** number2
print("Exponentiation:", result, type(result))

maths_marks = 85
science_marks = 78
english_marks = 90

total_marks = maths_marks + science_marks + english_marks
average_marks = total_marks / 3

print("Total marks:", total_marks)
print("Average marks:", average_marks)

product_price = 250
quantity = 4

total_price = product_price * quantity
print("Total price:", total_price)

number = 27

if number % 2 == 0:
    print("The number is even")
else:
    print("The number is odd")


a = 17
b = 5

print("Positive numbers:")
print("Normal division:", a / b)
print("Floor division:", a // b)

a = -17
b = 5

print("Negative numbers:")
print("Normal division:", a / b)
print("Floor division:", a // b)

a = -15
b = -4

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Floor division:", a // b)
print("Modulus:", a % b)

positive1 = 10
positive2 = 4
negative1 = -10
negative2 = -4

print("Positive - Positive:", positive1 - positive2)
print("Positive - Negative:", positive1 - negative2)
print("Negative - Positive:", negative1 - positive2)
print("Negative - Negative:", negative1 - negative2)

positive1 = 17
positive2 = 5
negative1 = -17
negative2 = -5

print("Positive // Positive:", positive1 // positive2)
print("Negative // Positive:", negative1 // positive2)
print("Positive // Negative:", positive1 // negative2)
print("Negative // Negative:", negative1 // negative2)

positive1 = 17
positive2 = 5
negative1 = -17
negative2 = -5

print("Positive % Positive:", positive1 % positive2)
print("Negative % Positive:", negative1 % positive2)
print("Positive % Negative:", positive1 % negative2)
print("Negative % Negative:", negative1 % negative2)

print("10 + 5 * 2 =", 10 + 5 * 2)
print("20 - 4 / 2 =", 20 - 4 / 2)
print("10 + 20 / 5 * 2 =", 10 + 20 / 5 * 2)
print("2 + 3 * 4 ** 2 =", 2 + 3 * 4 ** 2)
print("100 - 20 // 5 =", 100 - 20 // 5)


print("10 + 5 * 2 =", 10 + 5 * 2)
print("20 - 4 / 2 =", 20 - 4 / 2)
print("10 + 20 / 5 * 2 =", 10 + 20 / 5 * 2)
print("2 + 3 * 4 ** 2 =", 2 + 3 * 4 ** 2)
print("100 - 20 // 5 =", 100 - 20 // 5)


print("10 + 5 * 2 =", 10 + 5 * 2)
print("(10 + 5) * 2 =", (10 + 5) * 2)
print("20 - 10 / 2 =", 20 - 10 / 2)
print("(20 - 10) / 2 =", (20 - 10) / 2)
print("2 + 3 * 4 =", 2 + 3 * 4)
print("(2 + 3) * 4 =", (2 + 3) * 4)

a = True
b = False
result = a + b
print("Addition:", result, type(result))
result = a - b
print("Subtraction:", result, type(result))
result = a * b
print("Multiplication:", result, type(result))
result = a / 1
print("Division:", result, type(result))
result = a // 1
print("Floor division:", result, type(result))
result = a % 1
print("Modulus:", result, type(result))
result = a ** 2
print("Exponentiation:", result, type(result))


print("True + 5 =", True + 5)
print("False + 5 =", False + 5)
print("True * 10 =", True * 10)
print("False * 10 =", False * 10)
print("True - 5 =", True - 5)
print("False - 5 =", False - 5)

first_name = "Gayatri"
last_name = "Srivastava"
full_name = first_name + " " + last_name
print("Full name:", full_name)

word = "Hello"
print(word * 3)
try:
    print(word * 2.5)
except TypeError:
    print("A string cannot be multiplied by a float.")

text1 = "Hello"
text2 = "World"

print(text1 + text2)
print(text1 * 3)

try:
    print(text1 - text2)
except TypeError:
    print("String - String gives TypeError")

try:
    print(text1 / text2)
except TypeError:
    print("String / String gives TypeError")


value = None
number = 10

try:
    print(value + number)
except TypeError:
    print("Addition gives TypeError")

try:
    print(value - number)
except TypeError:
    print("Subtraction gives TypeError")

try:
    print(value * number)
except TypeError:
    print("Multiplication gives TypeError")

try:
    print(value / number)
except TypeError:
    print("Division gives TypeError")

try:
    print(value // number)
except TypeError:
    print("Floor division gives TypeError")

try:
    print(value % number)
except TypeError:
    print("Modulus gives TypeError")

try:
    print(value ** number)
except TypeError:
    print("Exponentiation gives TypeError")

try:
    print(10 / 0)
except ZeroDivisionError:
    print("Division by zero gives ZeroDivisionError")

try:
    print("Hello" - "World")
except TypeError:
    print("Subtracting strings gives TypeError")

try:
    value = None
    print(value + 10)
except TypeError:
    print("Arithmetic with None gives TypeError")

number1 = 25
number2 = 4

print("Addition:", number1 + number2)
print("Subtraction:", number1 - number2)
print("Multiplication:", number1 * number2)
print("Division:", number1 / number2)
print("Floor Division:", number1 // number2)
print("Modulus:", number1 % number2)
print("Exponentiation:", number1 ** number2)

a = 10
b = -3
c = 2.5
expression1 = a + b
print("1. a + b =", expression1)
expression2 = a - b
print("2. a - b =", expression2)
expression3 = b * c
print("3. b * c =", expression3)
expression4 = a / c
print("4. a / c =", expression4)
expression5 = a // b
print("5. a // b =", expression5)
expression6 = a % 3
print("6. a % 3 =", expression6)
expression7 = a ** 3
print("7. a ** 3 =", expression7)
expression8 = (a + b) + c
print("8. (a + b) + c =", expression8)
expression9 = a - b * c
print("9. a - b * c =", expression9)
expression10 = (a - b) / 2
print("10. (a - b) / 2 =", expression10)
expression11 = a + c / 2
print("11. a + c / 2 =", expression11)
expression12 = (a + b) * c
print("12. (a + b) * c =", expression12)