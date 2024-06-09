#5. Write a program which takes a number from user. Print Saurabh Shukla if the number is even, print Prateek Jain if the number is negative odd number and print Aditya Choudhary if number is positive odd number.
text = "Enter a Number"
num = int(input(text))
result = ""

if(num % 2 == 0):
    result = "even"
elif(num % 2 !=0 and num < 0):
    result = "negativeOdd"
elif(num % 2 != 0 and num > 0):
    result = "positiveOdd"
else:
    print("Invalid")
    
match(result):
    case "":
        print("Invalid Text")
    case "even":
        print("Saurabh Shukla") 
    case "negativeOdd":
        print("Prateek Jain")
    case"positiveOdd":
        print("Aditya Chaudhary")      