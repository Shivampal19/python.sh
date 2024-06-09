#6. Write a python program to check whether a given string is a multiword string or single word string using match case statement.
text = "Enter a string "
word = input(text)
count = 0
value = 0

for e in word:
    count+=1

if(count > 1):
    value = 1
    
match(value):
    case 0:
        print("single word string")
    case 1:
        print("multiword string")       