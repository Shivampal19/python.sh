#9. Write a python script to check whether a given year is a leap year or not.
y=int(input("Enter year Number"))
if y%400==0 or y%100!=0 and y%4==0:
    print("Leap Year")
else:
    print("Non Leap Year")   