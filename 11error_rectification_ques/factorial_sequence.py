#Write a program to add first seven terms of the following series using a for loop.
#  1/1! + 2/2! + 3/3! + … 
sum=0
for i in range (1,8):
            for j in range(2,9):
                sum=sum+ i/i*(j-1)

print(sum)
