# we know that the no of candies is less than 200 so
a= int(input("Amount left after dividing evenly in 5 people: "))# in example it is 2
b= int(input("Amount left after dividing evenly in 6 people: "))# in example it is 3
c= int(input("Amount left after dividing evenly in 7 people: "))# in example it is 2
for x in range(1,200):
    if(x%5==a and x%6==b and x%7==c):
        print("The no of candies is: ",x)
        break

