# Write a python script to print all prime numbers within a range start = 15, end = 45

givenRange = range(15, 45)

for e in givenRange:
    for i in range(2, e):
        if (e % i) == 0 :
            break
    else:
        print(e)