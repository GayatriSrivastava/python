#Take a user's age and Boolean variable has_id.
#Print Allowed only when:
#age >= 18
#and
#has_id is True
has_id=input("enter if he has id (yes/no): ").strip().lower()
if has_id=="no":
    print("pleasen bring your id")
elif(has_id=="yes"):
    print("welcome")
else:
    print("invalid input")






