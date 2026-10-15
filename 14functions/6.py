
def check_balance(existing_balance=3000):
    print("balance=",existing_balance)
def credit_balance(credit,existing_balance=3000):
    total_balance=credit+existing_balance
    print(total_balance)
def withdrawl_balance(widhraw,existing_balance=3000):
    total_balance=existing_balance-widhraw
    print(total_balance)

check_balance()
credit_balance(500)
withdrawl_balance(500)
credit_balance(500,1500)
withdrawl_balance(500,1500)
