#Write a program to find the range of a set of numbers entered through the keyboard.
#  Range is the difference between the smallest and biggest number in the list
numbers = list(map(int, input("Enter numbers separated by space: ").split()))
range_of_numbers = max(numbers) - min(numbers)
print("The range of the numbers is:", range_of_numbers)