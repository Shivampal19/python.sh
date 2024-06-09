#3. Write a menu driven program with the following options:
#a. Check whether a given set of three numbers are lengths of an isosceles triangle or not
text="""
1.isosceles triangle
2.right triangle
3.equilateral triangle
4.Exit

choose a number
"""
userInput=int(input(text))

match(userInput):
    case 1:
        print("you select isosceles triangle")
        print("Enter value of three side")
        p=int(input("Enter perpendicular value "))
        b=int(input("Enter base value "))
        h=int(input("Enter hypotenus value "))
        if((p==b) or (b==h) or (h==p)):
            print("This is isosceles triangle")
        else:
            print("This is not isosceles triangle")
    case 2:
        print("you select right triangle")
        print("Enter value of three side")
        p=int(input("Enter perpendicular value "))
        b=int(input("Enter base value "))
        h=int(input("Enter hypotenus value "))
        if(p**2+b**2 == h**2):
            print("This is right triangle")
        else:
            print("This is not right triangle")
    case 3:
        print("you select equilateral triangle")
        print("Enter value of three side")
        p=int(input("Enter perpendicular value "))
        b=int(input("Enter base value "))
        h=int(input("Enter hypotenus value "))
        if(p == b == h):
            print("This is equilateral triangle")
        else:
            print("This is not equilateral triangle")    
    case 4:
        Exit()