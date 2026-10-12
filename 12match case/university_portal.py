user = int(input("Enter user type: "))

match user:
    case 1:
        option = int(input("Enter option: "))
        match option:
            case 1:
                print("Opening Student Courses")
            case 2:
                print("Opening Student Marks")
            case 3:
                print("Opening Student Attendance")
            case _:
                print("Invalid Option")
    case 2:
        option = int(input("Enter option: "))
        match option:
            case 1:
                print("Opening Teacher Students")
            case 2:
                print("Opening Teacher Marks")
            case 3:
                print("Opening Teacher Attendance")
            case _:
                print("Invalid Option")
    case _:
        print("Invalid User Type")