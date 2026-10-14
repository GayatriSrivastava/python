#Given a sequence of integers, print numbers from left to right and stop when the first negative number is encountered. Do not print the negative number.
numbers=input("Enter numbers separated by spaces: ").split()
for i in numbers:
    if int(i)<0:
        break
    print(i)