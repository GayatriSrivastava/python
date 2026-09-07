age=map(int,input("Enter age: ").split())
for i in age:
    if i>=18:
        print("Adult")
    else:
        print("Minor")

