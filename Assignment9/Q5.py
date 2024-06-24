#5. Write a python script to print first N odd natural numbers in reverse order.

"""num = 1
i = 0
oddNum = int(input("Enter N natural Number "))

print('first N odd natural numbers in reverse order')
while(i <= oddNum):
    print(num)
    num = num -2
    
    i -= 1"""
    
# Write a python script to print first N odd natural numbers in reverse order. 

nNatural = int(input('Enter n number: '))

print('First {nNatural} Odd Numbers in Reverse Order:')
while(nNatural > 0):
    
    if(nNatural % 2 != 0):
        print(nNatural, end=" ")
    nNatural -=1