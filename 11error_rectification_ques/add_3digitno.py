#input a three digit number then take some of each digit.
num=int(input("Enter a three digit number: "))
first_digit=num//100
middle_digit=(num//10)%10
last_digit=num%10
sum=first_digit + middle_digit + last_digit
print("Sum of digits =",sum)

