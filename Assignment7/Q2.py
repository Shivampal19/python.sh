#2. Write a menu driven program to perform following operations - Addition, Subtraction,Multiplication, Division.
text = """
1.addition
2.substraction
3.multiplication
4.division 
5.Exit

choose a number
"""
userInuput=int(input(text))

match(userInuput):
    case 1:
        print("you choose addition")
        print("Enter two number")
        num1=int(input("first number "))
        num2=int(input("Second Number "))
        sum=num1+num2
        print(num1, "and", num2, "is", sum)
    case 2:
        print("you choose substraction")
        print("Enter two number")
        num1=int(input("first number "))
        num2=int(input("Second Number "))
        sub=num1-num2
        print(num1, "and", num2, "is", sub)
    case 3:
        print("you choose multipication")
        print("Enter two number")
        num1=int(input("first number "))
        num2=int(input("Second Number "))
        multi=num1*num2
        print(num1, "and", num2, "is", multi)
    case 4:
        print("you choose division")
        print("Enter two number")
        num1=int(input("first number "))
        num2=int(input("Second Number "))
        div=num1/num2
        print(num1, "and", num2, "is", div)
    case 5:
        exit()
        