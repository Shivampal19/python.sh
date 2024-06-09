#12. Write a python script to accept one complex number from the user and display the greater number between real part and imaginary part.
x=complex(input("Enter A Complex Number"))
if x.real > x.imag:
    print(x.real)
else:
    print(x.imag)    