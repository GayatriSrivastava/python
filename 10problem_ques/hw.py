#q 1
length=10
width=5
area=length*width
print(area)

#q 2
marks=int(input("Enter marks: "))
if marks>=40:
    print("Pass")
else:
    print("Fail")

#q 3
a=int(input())
b=int(input())
total=a+b
print(total)

#q 4
number=int(input())
if number%2==0:
    print("Even")
else:
    print("Odd")

#q 5
a=int(input())
b=int(input())
c=int(input())
total=a+b+c
average=total/3
print(average)

#q 6
celsius=float(input())
fahrenheit=(celsius*9/5)+32
print(fahrenheit)

#q 7
number=int(input())
if number>0:
    square=number*number
    print(square)
else:
    print("Invalid")

#q 8
a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
if a>b:
    print(a)
else:
    print(b)

#q 9
marks=int(input("Enter marks: "))
if marks>=90:
    print("A")
elif marks>=75:
    print("B")
elif marks>=50:
    print("C")
else:
    print("Fail")

#q 10
length=float(input("Enter length: "))
width=float(input("Enter width: "))
area=length*width
perimeter=2*(length+width)
print("Area:",area)
print("Perimeter:",perimeter)

#q 11
number=int(input("Enter a number: "))
if number>0:
    print("Positive")
elif number<0:
    print("Negative")
else:
    print("Zero")

#q 12
price=float(input("Enter price: "))
if price>=1000:
    discount=price*0.10
    final_price=price-discount
else:
    final_price=price
print(final_price)