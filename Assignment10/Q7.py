#7. Write a python script to print first N odd natural numbers

N = int(input("Enter N number "))
for a in range(1,(N)*2):
    if a % 2 != 0:
        print(a)