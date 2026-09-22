#Take 5 numbers from the user.
#For each number:
#Convert it to a string.
#Examine every digit using a loop.
#Count even and odd digits.
#Print which type occurs more.
#If equal, print "Equal".
for i in range(1, 6):
    number = input("Enter a number: ")
    even = 0
    odd = 0
    for ch in number:
        digit = int(ch)
        if digit % 2 == 0:
            even += 1
        else:
            odd += 1
    print("Even digits:", even)
    print("Odd digits:", odd)
    if even > odd:
        print("Even occurs more")
    elif odd > even:
        print("Odd occurs more")
    else:
        print("Equal")