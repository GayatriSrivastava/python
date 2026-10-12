order=int(input("enter your order:1.pizza 2.burger 3.sandwich 4.pasta:"))
match order:
    case 1:
        print("you have ordered pizza")
    case 2:
        print("you have ordered burger")
    case 3:
        print("you have ordered sandwich")  
    case 4:
        print("you have ordered pasta")
    case _:
        print("invalid order")