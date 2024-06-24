#4. Write a python script to print first N odd natural numbers.

Num = 1
i = 0
oddNum = int(input("Enter a number "))

print("first {oddNum} odd natural numbers")
while(i < oddNum):
    print(Num)
    Num = Num + 2
    
    i += 1
    