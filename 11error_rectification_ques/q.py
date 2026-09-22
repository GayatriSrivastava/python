has_id=input("Do you have an ID? Enter yes or no: ")

if has_id.lower()=="yes":
    has_id=True
    print("Welcome")

elif has_id.lower()=="no":
    has_id=False
    print("Bring an ID")

else:
    print("Invalid input")