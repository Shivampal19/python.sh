#8. Write a python script to check whether two given strings are identical, first string
#comes before the second in dictionary order or first string comes after the second
#string in dictionary order using match case statement

str1 = "sachin"
str2 = "shivam"
value = 0

if(str1 == str2):
    value = 1
elif(str1 > str2):
    value = 2
elif(str2 > str1):
    value = 3
    
match(value):
    case 1:
        print("Identical")
    case 2:
        print("Str1 is greater")
    case 3:
        print("Str2 is greater")    