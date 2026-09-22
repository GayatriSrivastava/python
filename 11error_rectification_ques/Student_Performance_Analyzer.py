#Take marks of 10 students using a for loop.
#For each student:
#Print "Fail" if marks are below 35.
#Print "Pass" for 35–49.
#Print "Good" for 50–74.
#Print "Excellent" for 75–100.
#At the end, print the number of students in each category.
fail=0
passed=0
good=0
execellent=0
for i in range(1,11):
    marks=int(input("enter marks of student:"))

if marks<35:
    print("fail")
elif marks <= 49:
        print("Pass")
        passed += 1
    elif marks <= 74:
        print("Good")
        good += 1
    elif marks <= 100:
        print("Excellent")
        excellent += 1
print("Pass:", passed)
print("Good:", good)
print("Fail:", fail)
print("Pass:", passed)
print("Good:", good)
print("Excellent:", excellent)
