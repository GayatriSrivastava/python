num=int(input("enter number:"))
if(num%2==0):
        if(num<0):
                print("negative even")
            

        elif(num>0):
            print("positive even")
        
    
elif(num%2!=0):
    
        if(num>0):
            print("positive odd")
        elif(num<0):
            print("negative odd")
    
else:
    print("invalid input")
    