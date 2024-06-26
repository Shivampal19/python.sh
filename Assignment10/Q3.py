# 3. Write a python script to print first M multiples of N.

m = int(input("Enter M Number "))
n = int(input("Enter N Number "))

for a in range(m):
   
    print((a+1)**n)