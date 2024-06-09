#7. Write a python program to check whether a given number is positive, negative or zero using match case statement.
num = int(input("Enter a Number "))
value = 0

if(num > 0):
    value = 1
elif(num < 0):
    value = 2
else:
    value = 3
    
match(value):
    case 1:
        print("positive")
    case 2:
        print("negative") 
    case 3:
        print("zero")