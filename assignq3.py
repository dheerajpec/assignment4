import random
for x in range(10):
    a= int(random.random()*10)
    b= int(random.random()*10)
    print(a,"x",b,"=")
    c=int(input())
    if(c==(a*b)):
        print("correct")
    else:
        print("incorrect")
        
