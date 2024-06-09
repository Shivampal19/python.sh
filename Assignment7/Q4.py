#4. Write a program which takes user’s age and display the category of person. Agebelow 10 years- Kid, Age below 20 - Teen, Age below 40 - young, Age below 60 -Experienced, Age above or equal 60 - Senior Citizen.
text = "Enter your age "
Age=int(input(text))
value=0
if(Age < 10):
    value = 1
elif(10 < Age < 20):
    value = 2
elif(20 < Age < 40):
    value = 3
elif(40 < Age < 60):
    value = 4  
elif(Age >= 60):
    value = 5 
else:
    value = 1
    
match(value):
    case 1:
        print("kid")  
    case 2:
        print("teen")
    case 3:
        print("young")
    case 4:
        print("Experienced")
    case 5:
        print("Senior Citizen")  
    case 1:
        print("wrong Age")                 