#1. Write a python script to display the number of days in a given month number.
m=int(input("Enter Month Number"))
if m in (1,3,5,7,8,10,12):
    print(31)
elif m in (4,6,9,11):
    print(30)
elif m in (2,2):
    print(28)
else:
    print("wrong input ")
    print()            