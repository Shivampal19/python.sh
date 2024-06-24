#3. Write a python script to print first N natural numbers in reverse order.
Num = int(input("Enter N Number "))
i = Num

print("first N natural numbers in reverse order ")
while(0 < i <= Num):
    print(i)
    i -= 1