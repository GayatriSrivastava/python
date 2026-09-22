#Take:
#Day
#Month
#Year
#Determine whether the date is valid.
year=int(input("enter year"))
month=int(input("enter month"))
day=int(input("enter day"))
if(year<0 or month<1 or month>12 or day<1 or day>31):
    print("invalid")
else:
        if(month==2):
                if((year%100==0 and year%400==0 ) or (year%100!=0 and year%4==0 )):
                        if(day<=29):
                               print("valid")
                        else:
                               print("invalid")
                else:
                        if(day<=28):
                               print("valid")
                        else:
                               print("invalid")
        elif(month==4 or month==6 or month==9 or month==11):
                if(day<=30):
                      print("valid")
                else:
                      print("invalid")
        elif(month==1 or month==3 or month ==5 or month==7 or month==10 or month==12):
                if(day<=31):
                      print("valid")
                else:
                       print("invalid")
                      
                      

