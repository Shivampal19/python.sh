#4. Write a python script to print the first 10 multiples of N in reverse order.

N = int(input("Enter N number "))

for a in range(10,1,-1):
    print(a**N)