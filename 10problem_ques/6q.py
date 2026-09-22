number=int(input())
if number==0:
    print("Zero")
elif number>0 and number%2==0:
    print("Positive Even")
elif number>0 and number%2!=0:
    print("Positive Odd")
elif number<0 and number%2==0:
    print("Negative Even")
else:
    print("Negative Odd")