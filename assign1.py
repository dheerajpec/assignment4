marks1=input("Enter the marks: ")
marks=int(marks1)
if(marks<25):
    print("You Got F grade")
elif (marks>=25 and marks<45):
    print("You Got D grade")
elif (marks>=45 and marks<60):
    print("You Got C grade")
elif (marks>=60 and marks<80):
    print("You Got B grade")
else:
    print("You got A")
