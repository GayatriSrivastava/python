num=int(input("enter num to call person you want to call:"))
match num:
    case 1:
        print("call teacher")
    case 2:
        print("call doctor")
    case 3:
        print("call plumber")
    case 4:
        print("call electrician")
    case _:
        print("invalid number")