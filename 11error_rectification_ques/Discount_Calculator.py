#Take purchase amount.
#Apply:
#Below ₹500       → 0%
#₹500–999         → 5%
#₹1000–1999       → 10%
#₹2000–4999       → 15%
#₹5000 and above  → 20%
#Print:
#Original amount
#Discount percentage
#Discount amount
#Final amount
quantity=int(input("enter quantity of product :"))
rate=int(input("enter rate of product :"))

amount=quantity*rate

if amount<500:
    discount=0
elif amount>=500 and amount<=999:
    discount=0.05
elif amount>=1000 and amount<=1999:
    discount=0.10
elif amount>=2000 and amount<=4999:
    discount=0.15
else:
    discount=0.20

discount_amount=amount*discount
final_amount=amount-discount_amount

print("Original amount:",amount)
print("Discount percentage:",discount*100,"%")
print("Discount amount:",discount_amount)
print("Final amount:",final_amount)