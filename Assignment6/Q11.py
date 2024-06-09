#11. Write a python script to take the month value in numeric format and display the number of days in it.
m=int(input("Enter month Number"))
if m in (1,3,5,7,8,10,12):
    print("31 Days")
elif m in (2,4,6,9,11):
    print("30 Days")
else:
    print("invalid month")    