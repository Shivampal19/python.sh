#9. Write a python script to check whether a given year is

text = """
A. Non century leap year
B. Century leap year
C. Non Century non leap year
D. century non leap year
"""


# A. Non century leap year : Year divisible not divided by 100 means Non-century year and non-century year divided by 4 is leap year.

# B. Century leap year : Year divided by 100 means century year and century year is divided by 400 is leap year

# C. Non century non leap year : Year not divided by 100 means non-century year and non-century year is divided by 4 means non-century non-leap year. 

# D.Century non leap year : Year divided by 100 means century year and century year is not divided by 400 means century non-leap year. 

print(text)
year = int(input("Enter a year "))
value = 0
if(year % 100 !=0 and year % 4 == 0):
    # Non century leap year
    value = 1
elif(year % 100 == 0 and year % 400 == 0):
    # Century leap year
    value = 2
elif(year % 100 !=0 and year % 4 != 0):
    # Non century non leap year
    value = 3
elif(year % 100 == 0 and year %400 !=0):
    # Century non leap year
    value = 4
else:
    value = ""
match(value):
    case 1:
        print("Non-century leap year") 
    case 2:
        print("Century leap year")
    case 3:
        print("Non-century non-leap year")
    case 4:
        print("Century non-leap year")
    case "":
        print("Invalid")




