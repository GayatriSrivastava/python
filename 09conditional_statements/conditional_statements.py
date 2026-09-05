#ques 1
num = int(input("Enter a number: "))
if num > 10:
    print("Greater than 10")

#ques 2
age = int(input("Enter age: "))
if age >= 18:
    print("Adult")

#ques 3
num = int(input("Enter a number: "))
if num > 0:
    print("Positive")

#ques 4
marks = int(input("Enter marks: "))
if marks >= 40:
    print("Pass")

#ques 5
num = int(input("Enter a number: "))
if num == 0:
    print("Zero")

#ques 6
num = int(input("Enter a number: "))
if num > 0:
    print("Positive")
else:
    print("Not positive")

#ques 7
age = int(input("Enter age: "))
if age >= 18:
    print("Adult")
else:
    print("Minor")

#ques 8
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Even")
else:
    print("Odd")

#ques 9
marks = int(input("Enter marks: "))
if marks >= 40:
    print("Pass")
else:
    print("Fail")

#ques 10
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
if a > b:
    print(f"{a} is greater")
else:
    print(f"{b} is greater")

#ques 11
marks = int(input("Enter marks: "))
if marks >= 90:
    print("A")
elif marks >= 75:
    print("B")
elif marks >= 60:
    print("C")
elif marks >= 40:
    print("D")
else:
    print("F")

#ques 12
num = int(input("Enter a number: "))
if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")

#ques 13
day = int(input("Enter day number: "))
if day == 1:
    print("Monday")
elif day == 2:
    print("Tuesday")
elif day == 3:
    print("Wednesday")
elif day == 4:
    print("Thursday")
elif day == 5:
    print("Friday")
else:
    print("Other")

#ques 14
marks = int(input("Enter marks: "))
if marks >= 75:
    print("Excellent")
elif marks >= 60:
    print("Good")
elif marks >= 40:
    print("Pass")
else:
    print("Fail")

#ques 15
num = int(input("Enter a number: "))
if num == 1:
    print("1")
elif num == 2:
    print("2")
elif num == 3:
    print("3")
else:
    print("Other")

#ques 16
age = int(input("Enter age: "))
if age >= 18:
    if age <= 60:
        print("Between 18 and 60")

#ques 17
marks = int(input("Enter marks: "))
if marks >= 40:
    if marks >= 75:
        print("Good")
    else:
        print("Passed")
else:
    print("Failed")

#ques 18
num = int(input("Enter a number: "))
if num > 0:
    if num > 100:
        print("Greater than 100")
    else:
        print("Positive but not greater than 100")

#ques 19
age = int(input("Enter age: "))
if age >= 18:
    if age >= 60:
        print("Senior citizen")
    else:
        print("Adult")
else:
    print("Minor")

#ques 20
num = int(input("Enter a number: "))
if num != 0:
    if num > 0:
        print("Positive")
    else:
        print("Negative")
else:
    print("Zero")

#ques 21
age = int(input("Enter age: "))
marks = int(input("Enter marks: "))
if age >= 18 and marks >= 40:
    print("Eligible")

#ques 22
num = int(input("Enter a number: "))
if num < 10 or num > 100:
    print("Special")

#ques 23
age = int(input("Enter age: "))
has_id = input("Do you have ID? True/False: ") == "True"
if age >= 18 and has_id is True:
    print("Allowed")

#ques 24
first = int(input("Enter first number: "))
second = int(input("Enter second number: "))
if first > 10 and second > 10:
    print("Both are greater than 10")

#ques 25
num = int(input("Enter a number: "))
if num < 0 or num > 100:
    print("Outside range")

#ques 26
is_closed = False
if not is_closed:
    print("Open")

#ques 27
num = int(input("Enter a number: "))
if num >= 10 and num <= 50:
    print("Between 10 and 50")

#ques 28
num = int(input("Enter a number: "))
if num < 10 or num > 50:
    print("Outside the range")

#ques 29
is_student = True
has_id = True
has_ticket = True
if is_student and has_id and has_ticket:
    print("Allowed")

#ques 30
age = int(input("Enter age: "))
marks = int(input("Enter marks: "))
has_id = input("Do you have ID? True/False: ") == "True"
if age >= 18 and marks >= 40 and has_id is True:
    print("Eligible")
else:
    print("Not eligible")

