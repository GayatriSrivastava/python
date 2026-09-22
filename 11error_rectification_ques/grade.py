total=0
flag=True
grade="F"

for i in range(5):
    marks=(int(input("enter number")))
    total+=marks
    if marks<35:
        flag= False
    else:
        flag=True
        if marks>=90:
            grade="A+"
            print(grade)
        elif marks>=80 and marks<=89:
            grade="A"
            print(grade)
        elif marks>=70 and marks<=79:
            grade="B"
            print(grade)
        elif marks>=60 and marks<=69:
            grade="c"
            print(grade)
        