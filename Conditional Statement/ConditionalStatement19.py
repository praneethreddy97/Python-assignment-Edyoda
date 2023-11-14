"""Write a program to find the largest number out of two numbers excepted from user."""

a=int(input("Enter first number\n"))

b=int(input("Enter Second number\n"))

c=int(input("Enter third number\n"))

if a>b and a>c:
    print(a," is a largest number")
elif b>c:
    print(b," is a largest number")
else:
    print(c," is a largest number")
