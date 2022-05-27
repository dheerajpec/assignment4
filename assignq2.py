year= int(input("Enter the year: "))
if(year%4==0):
    if(year%100==0):
        if(year%400==0):
            print("The entered year is leap year")
        else:
            print("The entered year is not a leap year")# as it is given that year divisible by 100 should also be divisible by 400
    else:
         print("The entered year is a leap year")
else:
    print("The entered year is a leap year")
            
