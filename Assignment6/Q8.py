#8. Write a python script to check whether a given quadratic equation has two real & distinct roots, real & equal roots or imaginary roots.
a=int(input("Enter First Number"))
b=int(input("Enter Second Number"))
c=int(input("Enter Third Number"))
x=b**2-4*a*c
if x>0:
    print("Real and Distrinct Roots")
elif x==0:
    print("Real and Equal Roots")
else:
    print("imaginary Roots")        