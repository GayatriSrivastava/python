#q1
for i in range(5):
    print("Hello")

#q2
for i in range(10):
    print(i, end=" ")
print()

#q3
for i in range(1, 11):
    print(i, end=" ")
print()

#q4
for i in range(10, 0, -1):
    print(i, end=" ")
print()

#q5
for i in range(5, 51, 5):
    print(i, end=" ")
print()

#q6
for i in range(2, 21, 2):
    print(i, end=" ")
print()

#q7
for i in range(1, 20, 2):
    print(i, end=" ")
print()

#q8
for i in range(3, 19, 3):
    print(i, end=" ")
print()

#q9
for i in range(20, 1, -2):
    print(i, end=" ")
print()

#q10
n = int(input("Enter n: "))
for i in range(1, n + 1):
    print(i, end=" ")
print()

#q11
n = int(input("Enter n: "))
for i in range(1, n + 1):
    if i % 2 == 0:
        print(i, end=" ")
print()

#q12
n = int(input("Enter n: "))
for i in range(1, n + 1):
    if i % 2 != 0:
        print(i, end=" ")
print()

#q13
n = int(input("Enter n: "))
for i in range(1, n + 1):
    if i % 3 == 0:
        print(i, end=" ")
print()

#q14
n = int(input("Enter n: "))
for i in range(1, n + 1):
    if i % 2 == 0 and i % 3 == 0:
        print(i, end=" ")
print()

#q15
n = int(input("Enter n: "))
count = 0
for i in range(1, n + 1):
    if i % 2 == 0:
        count += 1
print("Even numbers:", count)

#q16
n = int(input("Enter n: "))
total = 0
for i in range(1, n + 1):
    total += i
print("Sum:", total)

#q17
n = int(input("Enter n: "))
total = 0
for i in range(1, n + 1):
    if i % 2 == 0:
        total += i
print("Sum of even numbers:", total)

#q18
n = int(input("Enter n: "))
total = 0
for i in range(1, n + 1):
    if i % 2 != 0:
        total += i
print("Sum of odd numbers:", total)

#q19
n = int(input("Enter a number: "))
for i in range(1, 11):
    print(n, "x", i, "=", n * i)

#q20
n = int(input("Enter n: "))
product = 1
for i in range(1, n + 1):
    product *= i
print("Product:", product)

#q21
text = input("Enter a string: ")
for ch in text:
    print(ch)

#q22
text = input("Enter a string: ")
for ch in text:
    print(ch, end="")
print()

#q23
text = input("Enter a string: ")
count = 0
for ch in text:
    count += 1
print("Characters:", count)

#q24
text = input("Enter a string: ")
count = 0
for ch in text:
    if ch == "a":
        count += 1
print("a appears:", count)

#q25
text = input("Enter a string: ")
count = 0
for ch in text:
    if ch.isupper():
        count += 1
print("Uppercase letters:", count)

#q26
for i in range(3):
    for j in range(4):
        print("*", end="")
    print()

#q27
for i in range(4):
    for j in range(5):
        print("*", end="")
    print()

#q28
for i in range(1, 6):
    for j in range(i):
        print("*", end="")
    print()

#q29
for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end="")
    print()

#q30
for i in range(1, 6):
    for j in range(1, 6):
        print(i * j, end="\t")
    print()

#challenge
n = int(input("Enter n: "))
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end="")
    print()