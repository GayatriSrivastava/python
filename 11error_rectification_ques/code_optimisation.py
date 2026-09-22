#commputer ka time bachane ke liye ye time complexity ka code hai
operation=int(input("Enter the operation you want to perform: 1.addition 2.subtraction 3.multiplication 4.division 5.floor division: "))
if operation==1 or operation==2 or operation==3 or operation==4 or operation==5:
    a=int(input("Enter first number: "))
    b=int(input("Enter second number: "))
    if operation==1:
        print(f"Addition of {a} and {b} is: {a+b}")
    elif operation==2:
        print(f"Subtraction of {a} and {b} is: {a-b}")
    elif operation==3:
        print(f"Multiplication of {a} and {b} is: {a*b}")
    elif operation==4:
        print(f"Division of {a} and {b} is: {a/b}")
    elif operation==5:
        print(f"Floor division of {a} and {b} is: {a//b}") 
else:
    print("Invalid operation selected. Please choose a number between 1 and 5.")