#read two numbers display menu of operations read choice of operation perform operation and return operation and display default also do it with while loop and match case display menu again then take choice again and perform operation until zero for exit is entered
num1=int(input("enter num1:"))
num2=int(input("enter num2:"))

choice=1
while choice != 0:
    choice=int(input("enter choice:1.add 2.sub 3.mul 4.div 0.exit:"))


    match choice:
        case 1:
            print("result:",num1+num2)
        case 2:
            print("result:",num1-num2)
        case 3:
            print("result:",num1*num2)
        case 4:
            print("result:",num1/num2)
        case 0:
            print("Exiting...")
        case _:
            print("Invalid choice")

#or
num1=int(input("enter num1:"))
num2=int(input("enter num2:"))
choice=int(input("enter choice:1.add 2.sub 3.mul 4.div 0.exit:"))
while True:
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("0. Exit")

    choice=int(input("enter choice:"))

    match choice:
        case 1:
            print("result:",num1+num2)
        case 2:
            print("result:",num1-num2)
        case 3:
            print("result:",num1*num2)
        case 4:
            print("result:",num1/num2)
        case 0:
            print("Exiting...")
            break
        case _:
            print("Invalid choice")