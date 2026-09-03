#ques 18
print(True and True)
print(True and False)
print(False and True)
print(False and False)

#ques 19
print(True or True)
print(True or False)
print(False or True)
print(False or False)

#ques 20
print(not True)
print(not False)

#ques 21
# and: True only when both conditions are True
# or: True when at least one condition is True
# not: Reverses the Boolean result

#ques 22
age = 25
print(age >= 18)
print(age <= 60)
print(age >= 18 and age <= 60)

#ques 23
age = 16
print(age < 18)
print(age > 60)
print(age < 18 or age > 60)

#ques 24
age = 20
print(age < 18)
print(not age < 18)

#ques 25
num = int(input("Enter a number: "))
print(num > 10 and num < 50)

#ques 26
num = int(input("Enter a number: "))
print(num < 10 or num > 100)

#ques 27
num = int(input("Enter a number: "))
print(num > 10)
print(not num > 10)

#ques 28
print(bool(0))
print(bool(1))
print(bool(-5))
print(bool(""))
print(bool("Python"))
print(bool(False))
print(bool(True))
print(bool(None))

#ques 29
print(bool(0))
print(bool(10))
print(bool(""))
print(bool("Hello"))
print(bool(None))

#ques 30
values = [0, 1, "", "Python", False, None]
for value in values:
    print(value, type(value), bool(value))