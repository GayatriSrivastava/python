# ATM Withdrawal
#Take:
#Account balance
#Withdrawal amount
#Rules:
#Withdrawal amount must be greater than 0.
#Withdrawal amount must be divisible by 100.
#Withdrawal amount cannot be greater than the balance.
#After withdrawal, at least ₹500 must remain.
balance=float(input())
withdrawal=float(input())
if withdrawal<=0:
    print("Invalid withdrawal amount")
elif withdrawal%100!=0:
    print("Withdrawal amount must be divisible by 100")
elif withdrawal>balance:
    print("Insufficient balance")
elif balance-withdrawal<500:
    print("At least 500 must remain")
else:
    remaining=balance-withdrawal
    print("Withdrawal successful")
    print("Remaining balance:",remaining)