#Calculate electricity bill based on units.
#Rules:First 100 units → ₹5 per unit 
#Next 100 units → ₹7 per unit
#Above 200 units → ₹10 per unit
bill=0
unit=int(input("enter meter unit:"))

if unit<=100:
    print(bill=5*unit)
elif unit<=200:
    print(bill=100*5+(unit-100)*7)
else:
    print(bill=100*5+100*7+(unit-200)*10)
