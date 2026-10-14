#Q1
marks=int(input("Enter marks: "))
while marks<0 or marks>100:
    marks=int(input("Enter marks between 0 and 100: "))
print(marks)

#Q2
n=int(input("Enter a positive integer: "))
while n<=0:
    n=int(input("Enter a positive integer: "))
print(n)

#Q3
age=int(input("Enter age: "))
while age<0 or age>120:
    print("Invalid age")
    age=int(input("Enter age between 0 and 120: "))
print(age)

#Q4
print("1. View profile\n2. Edit profile\n3. Settings\n4. Exit")
choice=int(input("Enter choice: "))
while choice<1 or choice>4:
    print("Invalid choice")
    choice=int(input("Enter choice: "))
print("Selected option:",choice)

#Q5
password=input("Enter password: ")
while len(password.strip())<8:
    password=input("Enter password with at least 8 characters: ")
print("Password accepted")

#Q6
temp=float(input("Enter temperature: "))
while temp<-20 or temp>45:
    temp=float(input("Enter temperature between -20 and 45: "))
print(temp)

#Q7
balance=5000
amount=float(input("Enter withdrawal amount: "))
while amount<=0 or amount>balance:
    amount=float(input("Enter a valid withdrawal amount: "))
balance-=amount
print("Remaining balance:",balance)

#Q8
username=input("Enter username: ").strip()
while len(username)<5 or " " in username:
    username=input("Enter a valid username: ").strip()
print("Accepted username:",username)

#Q9
n=int(input("Enter a positive number divisible by 3 and 5: "))
while n<=0 or n%3!=0 or n%5!=0:
    n=int(input("Enter a valid number: "))
print(n)

#Q10
pin=2468
attempts=0
while attempts<3:
    entered=int(input("Enter PIN: "))
    if entered==pin:
        print("Access granted")
        break
    attempts+=1
if attempts==3:
    print("Access denied")

#Q11
n=int(input("Enter an integer between 10 and 50: "))
while n<10 or n>50:
    n=int(input("Enter an integer between 10 and 50: "))
if n%2==0:
    print("Even")
else:
    print("Odd")

#Q12
balance=2000
amount=float(input("Enter deposit amount: "))
while amount<=0:
    amount=float(input("Enter a positive deposit amount: "))
balance+=amount
print("New balance:",balance)

#Q13
n=int(input("Enter an integer between 1 and 100: "))
while n<1 or n>100:
    n=int(input("Enter an integer between 1 and 100: "))
print(n)

#Q14
marks=int(input("Enter marks: "))
while marks<0 or marks>100:
    marks=int(input("Enter marks between 0 and 100: "))
if marks>=75:
    print("Distinction")
elif marks>=60:
    print("First Class")
elif marks>=35:
    print("Pass")
else:
    print("Fail")

#Q15
username=input("Enter username: ").strip()
password=input("Enter password: ")
while len(username)<5 or " " in username or len(password.strip())<8:
    print("Invalid username or password")
    username=input("Enter username: ").strip()
    password=input("Enter password: ")
print("Login details accepted")

#Q16
a=float(input("Enter first number: "))
op=input("Enter operator (+, -, *, /): ")
while op not in ["+","-","*","/"]:
    op=input("Enter a valid operator: ")
b=float(input("Enter second number: "))
while op=="/" and b==0:
    b=float(input("Enter a non-zero second number: "))
if op=="+":
    print(a+b)
elif op=="-":
    print(a-b)
elif op=="*":
    print(a*b)
else:
    print(a/b)

#Q17
balance=10000
choice=0
while choice!=4:
    print("1. Check balance\n2. Deposit money\n3. Withdraw money\n4. Exit")
    choice=int(input("Enter choice: "))
    if choice==1:
        print("Balance:",balance)
    elif choice==2:
        amount=float(input("Enter deposit amount: "))
        while amount<=0:
            amount=float(input("Enter a positive amount: "))
        balance+=amount
        print("New balance:",balance)
    elif choice==3:
        amount=float(input("Enter withdrawal amount: "))
        while amount<=0 or amount>balance:
            amount=float(input("Enter a valid withdrawal amount: "))
        balance-=amount
        print("New balance:",balance)
    elif choice==4:
        print("Exited")
    else:
        print("Invalid choice")

#Q18
month=int(input("Enter month (1-12): "))
day=int(input("Enter day (1-31): "))
while month<1 or month>12 or day<1 or day>31:
    print("Invalid month or day")
    month=int(input("Enter month (1-12): "))
    day=int(input("Enter day (1-31): "))
print("Month:",month,"Day:",day)

#Q19
quantity=int(input("Enter quantity: "))
while quantity<=0:
    quantity=int(input("Enter a positive quantity: "))
price=float(input("Enter unit price: "))
while price<=0:
    price=float(input("Enter a positive price: "))
print("Total cost:",quantity*price)

#Q20
count=int(input("How many numbers (1-20)? "))
while count<1 or count>20:
    count=int(input("Enter a count from 1 to 20: "))
total=0
for i in range(count):
    n=float(input("Enter a number: "))
    total+=n
print("Average:",total/count)

#Q21
password=input("Enter password: ")
while len(password)<8 or not any(i.isupper() for i in password) or not any(i.islower() for i in password) or not any(i.isdigit() for i in password) or any(i.isspace() for i in password):
    if len(password)<8:
        print("Password must contain at least 8 characters")
    if not any(i.isupper() for i in password):
        print("Password must contain an uppercase letter")
    if not any(i.islower() for i in password):
        print("Password must contain a lowercase letter")
    if not any(i.isdigit() for i in password):
        print("Password must contain a digit")
    if any(i.isspace() for i in password):
        print("Password must not contain spaces")
    password=input("Enter password again: ")
print("Strong password")

#Q22
n=int(input("Enter an integer from 1 to 10: "))
while n<1 or n>10:
    n=int(input("Enter an integer from 1 to 10: "))
print(n)

#Q23
a=int(input("Enter first score: "))
while a<0 or a>100:
    a=int(input("Enter first score between 0 and 100: "))
b=int(input("Enter second score: "))
while b<0 or b>100:
    b=int(input("Enter second score between 0 and 100: "))
c=int(input("Enter third score: "))
while c<0 or c>100:
    c=int(input("Enter third score between 0 and 100: "))
total=a+b+c
print("Total:",total)
print("Average:",total/3)

#Q24
balance=10000
amount=int(input("Enter withdrawal amount: "))
while amount<=0 or amount>balance or amount%100!=0:
    amount=int(input("Enter a positive amount, within balance, divisible by 100: "))
balance-=amount
print("Withdrawn amount:",amount)
print("Remaining balance:",balance)