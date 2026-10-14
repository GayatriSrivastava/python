#Take an integer limit. Print numbers from 1 through limit, but stop before printing 7.
#If limit is less than 7, print all numbers up to limit.
#Test cases
#Input Expected output
#10 1 2 3 4 5 6 5 1 2 3 4 5 7 1 2 3 4 5 6
#Print the numbers on one line, separated by spaces.
limit = int(input())
for i in range(1, limit + 1):
    if i == 7:
        break
    print(i, end=" ")