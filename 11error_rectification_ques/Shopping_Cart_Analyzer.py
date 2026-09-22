#Take prices of 8 products.
#For every price:
#Below 500 → "Budget"
#500–1999 → "Regular"
#2000–4999 → "Premium"
#5000 or more → "Luxury"
#Calculate:
#Total amount.
#Number of products in each category.
#Average product price.
#ques8
total = 0
budget = 0
regular = 0
premium = 0
luxury = 0
for i in range(1, 9):
    price = int(input("Enter price: "))
    total += price
    if price < 500:
        print("Budget")
        budget += 1
    elif price <= 1999:
        print("Regular")
        regular += 1
    elif price <= 4999:
        print("Premium")
        premium += 1
    else:
        print("Luxury")
        luxury += 1
average = total / 8
print("Total amount:", total)
print("Budget products:", budget)
print("Regular products:", regular)
print("Premium products:", premium)
print("Luxury products:", luxury)
print("Average price:", average)