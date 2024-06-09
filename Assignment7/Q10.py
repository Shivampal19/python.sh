#10. Write a program to display day name on the basis of user’s liking of a colour. Ask user for his favorite colour.

text1 = """ User can answer in a sentence like “I like red colour”.Assuming all colour name entered by user is in lowercase. """


text2 = """
a. Yellow - Monday
b. Blue - Tuesday
c. Orange - Wednesday
d. White - Thursday
e. Black - Friday
f. Red - Saturday
g. All other colours - Sunday
"""


string = input(text1)
colour = ""

if("yellow" in string):
    colour = "yellow"
elif("blue" in string):
    colour = "blue"
elif("orange" in string):
    colour = "orange"
elif("White" in string):
    colour = "white"
elif("black" in string):
    colour = "black"
elif("red" in string):
    colour = "Red"
else:
    colour = "other"
    
match(colour):
    case "yellow":
        print("monday")
    case "blue":
        print("Tuesday")
    case "orange":
        print("Wednesday")
    case "white":
        print("Thrusday")
    case "black":
        print("Friday")
    case "Red":
        print("Saturday")
    case "other":
        print("Sunday")    