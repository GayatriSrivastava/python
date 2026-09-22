#enter two numbers and perform these operation on them : 1.addition 2.subtraction 3.multiplication 4.division 5.floor division
a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
c=int(input("Enter the number corresponding to the operation you want to perform: 1.addition 2.subtraction 3.multiplication 4.division 5.floor division: "))
if c==1:
    print(f"Addition of {a} and {b} is: {a+b}")
elif c==2:
    print(f"Subtraction of {a} and {b} is: {a-b}")
elif c==3:
    print(f"Multiplication of {a} and {b} is: {a*b}")
elif c==4:
    print(f"Division of {a} and {b} is: {a/b}")
elif c==5:
    print(f"Floor division of {a} and {b} is: {a//b}")