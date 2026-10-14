#Simple menu-like program using pass
choice=int(input("1. Start\n2. Settings\n3. Exit\nEnter your choice: "))
if choice==1:
    print("Program started")
elif choice==2:
    pass
elif choice==3:
    print("Exiting")
else:
    print("Invalid choice")
print("Program closed")