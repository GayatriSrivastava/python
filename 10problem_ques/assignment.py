#q 1
number=int(input())
if number>0:
    print("Positive")
elif number<0:
    print("Negative")
else:
    print("Zero")

#q 2
number=int(input())
if number==0:
    print("Zero")
elif number>0 and number%2==0:
    print("Positive Even")
elif number>0 and number%2!=0:
    print("Positive Odd")
elif number<0 and number%2==0:
    print("Negative Even")
else:
    print("Negative Odd")

#q 3
a=int(input())
b=int(input())
if a>b:
    print(a)
elif b>a:
    print(b)
else:
    print("Both are equal")

#q 4
a=int(input())
b=int(input())
c=int(input())
if a<b and a<c:
    print(a)
elif b<a and b<c:
    print(b)
else:
    print(c)

#q 5
a=int(input())
b=int(input())
c=int(input())
if a>b and a>c:
    print(a,"is the largest")
elif b>a and b>c:
    print(b,"is the largest")
else:
    print(c,"is the largest")

#q 6
number=int(input())
if number%5==0 and number%11==0:
    print("Divisible by both 5 and 11")
elif number%5==0:
    print("Divisible only by 5")
elif number%11==0:
    print("Divisible only by 11")
else:
    print("Divisible by neither")

#q 7
number=int(input())
if number%3==0 and number%7==0:
    print("Divisible by both 3 and 7")
elif number%3==0:
    print("Divisible only by 3")
elif number%7==0:
    print("Divisible only by 7")
else:
    print("Divisible by neither")

#q 8
marks=int(input())
if marks<0 or marks>100:
    print("Invalid marks")
elif marks>=40:
    print("Pass")
else:
    print("Fail")

#q 9
marks=int(input())
if marks<0 or marks>100:
    print("Invalid marks")
elif marks>=90:
    print("A")
elif marks>=80:
    print("B")
elif marks>=70:
    print("C")
elif marks>=60:
    print("D")
elif marks>=40:
    print("E")
else:
    print("Fail")

#q 10
age=int(input())
if age<0 or age>120:
    print("Invalid age")
elif age<18:
    print("Cannot vote")
else:
    print("Can vote")

#q 11
year=int(input())
if year%400==0 or (year%4==0 and year%100!=0):
    print("Leap year")
else:
    print("Not a leap year")

#q 12
character=input()
if character>="A" and character<="Z":
    print("Uppercase alphabet")
elif character>="a" and character<="z":
    print("Lowercase alphabet")
elif character>="0" and character<="9":
    print("Digit")
else:
    print("Special character")

#q 13
character=input()
if character>="a" and character<="z" or character>="A" and character<="Z":
    if character=="a" or character=="e" or character=="i" or character=="o" or character=="u" or character=="A" or character=="E" or character=="I" or character=="O" or character=="U":
        print("Vowel")
    else:
        print("Consonant")
else:
    print("Invalid input")

#q 14
cost_price=float(input())
selling_price=float(input())
if selling_price>cost_price:
    profit=selling_price-cost_price
    print("Profit =",profit)
elif selling_price<cost_price:
    loss=cost_price-selling_price
    print("Loss =",loss)
else:
    print("No profit and no loss")

#q 15
cost_price=float(input())
selling_price=float(input())
if cost_price<=0:
    print("Invalid cost price")
elif selling_price>cost_price:
    profit=selling_price-cost_price
    percentage=profit/cost_price*100
    print("Profit =",profit)
    print("Profit percentage =",percentage)
elif selling_price<cost_price:
    loss=cost_price-selling_price
    percentage=loss/cost_price*100
    print("Loss =",loss)
    print("Loss percentage =",percentage)
else:
    print("No profit and no loss")

#q 16
units=int(input())
if units<0:
    print("Invalid units")
elif units<=100:
    bill=units*5
    print(bill)
elif units<=200:
    bill=100*5+(units-100)*7
    print(bill)
else:
    bill=100*5+100*7+(units-200)*10
    print(bill)

#q 17
a=float(input())
b=float(input())
operator=input()
if operator=="+":
    print(a+b)
elif operator=="-":
    print(a-b)
elif operator=="*":
    print(a*b)
elif operator=="/":
    if b==0:
        print("Cannot divide by zero")
    else:
        print(a/b)
else:
    print("Invalid operator")

#q 18
temperature=float(input())
if temperature<0:
    print("Freezing")
elif temperature<=15:
    print("Very Cold")
elif temperature<=25:
    print("Cold")
elif temperature<=35:
    print("Normal")
else:
    print("Hot")

#q 19
number=int(input())
if number<0:
    print("Negative")
elif number<=10:
    print("0-10")
elif number<=50:
    print("11-50")
elif number<=100:
    print("51-100")
else:
    print("Above 100")

#q 20
a=int(input())
b=int(input())
c=int(input())
if a+b>c and a+c>b and b+c>a:
    print("Valid triangle")
else:
    print("Invalid triangle")

#q 21
a=int(input())
b=int(input())
c=int(input())
if a+b<=c or a+c<=b or b+c<=a:
    print("Invalid triangle")
elif a==b and b==c:
    print("Equilateral")
elif a==b or b==c or a==c:
    print("Isosceles")
else:
    print("Scalene")

#q 22
balance=float(input())
withdrawal=float(input())
if withdrawal<=0:
    print("Invalid withdrawal amount")
elif withdrawal%100!=0:
    print("Withdrawal amount must be divisible by 100")
elif withdrawal>balance:
    print("Insufficient balance")
elif balance-withdrawal<500:
    print("At least 500 must remain")
else:
    remaining=balance-withdrawal
    print("Withdrawal successful")
    print("Remaining balance:",remaining)

#q 23
username=input()
password=input()
if username!="admin":
    print("User not found")
elif password!="python123":
    print("Wrong password")
else:
    print("Login successful")

#q 24
amount=float(input())
if amount<500:
    discount_percent=0
elif amount<1000:
    discount_percent=5
elif amount<2000:
    discount_percent=10
elif amount<5000:
    discount_percent=15
else:
    discount_percent=20
discount_amount=amount*discount_percent/100
final_amount=amount-discount_amount
print("Original amount:",amount)
print("Discount percentage:",discount_percent)
print("Discount amount:",discount_amount)
print("Final amount:",final_amount)

#q 25
marks1=float(input())
marks2=float(input())
marks3=float(input())
if marks1<0 or marks1>100 or marks2<0 or marks2>100 or marks3<0 or marks3>100:
    print("Invalid marks")
elif marks1<35 or marks2<35 or marks3<35:
    print("Fail")
else:
    average=(marks1+marks2+marks3)/3
    print("Average:",average)
    if average>=75:
        print("Distinction")
    elif average>=60:
        print("First Class")
    elif average>=50:
        print("Second Class")
    else:
        print("Pass")

#q 26
day=int(input())
month=int(input())
year=int(input())
if year<=0 or month<1 or month>12 or day<1:
    print("Invalid date")
elif month==2:
    if year%400==0 or (year%4==0 and year%100!=0):
        if day<=29:
            print("Valid")
        else:
            print("Invalid")
    else:
        if day<=28:
            print("Valid")
        else:
            print("Invalid")
elif month==4 or month==6 or month==9 or month==11:
    if day<=30:
        print("Valid")
    else:
        print("Invalid")
else:
    if day<=31:
        print("Valid")
    else:
        print("Invalid")

#q 27
hours=int(input())
minutes=int(input())
seconds=int(input())
if hours>=0 and hours<=23 and minutes>=0 and minutes<=59 and seconds>=0 and seconds<=59:
    print("Valid time")
else:
    print("Invalid time")

#q 28
name1=input()
age1=int(input())
name2=input()
age2=int(input())
name3=input()
age3=int(input())
if age1<age2 and age1<age3:
    print(name1,"is the youngest")
elif age2<age1 and age2<age3:
    print(name2,"is the youngest")
elif age3<age1 and age3<age2:
    print(name3,"is the youngest")
elif age1==age2 and age2==age3:
    print("All three have the same age")
elif age1==age2:
    print(name1,"and",name2,"have the same age and are the youngest")
elif age1==age3:
    print(name1,"and",name3,"have the same age and are the youngest")
else:
    print(name2,"and",name3,"have the same age and are the youngest")

#q 29
a=int(input())
b=int(input())
c=int(input())
if (a>b and a<c) or (a>c and a<b):
    print(a)
elif (b>a and b<c) or (b>c and b<a):
    print(b)
else:
    print(c)

#q 30
age=int(input())
marks=int(input())
income=int(input())
attendance=float(input())
if age>=18 and age<=25 and marks>=85 and attendance>=75 and income<=300000:
    print("Scholarship Approved")
else:
    print("Scholarship Rejected")
    if age<18 or age>25:
        print("Reason: Age not between 18 and 25")
    if marks<85:
        print("Reason: Marks below 85")
    if attendance<75:
        print("Reason: Attendance below 75")
    if income>300000:
        print("Reason: Family income above 300000")