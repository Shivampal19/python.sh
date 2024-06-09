#6. Write a python script which takes a three digit number from the user and displays only its middle digit.
x=int(input("Enter three digit number "))
a=int(x/10%10)
print(a)