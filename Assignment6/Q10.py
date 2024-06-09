#10. Write a python script to print greater among three numbers. Print number only once even if the numbers are the same.
a=int(input("Enter First number"))
b=int(input("Enter Second number"))
c=int(input("Enter Third number")) 
print((a if a>c else c) if a>b else (b if b>c else c))      