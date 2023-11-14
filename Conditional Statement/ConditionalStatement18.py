"""Write a program to whether a number (accepted from user) is divisible by 2 and 3 both."""

number=int(input("enter any number"))

if number % 2 == 0 and number % 3 == 0:
    print("it is divisible by 2 and 3")
else:
    print("it is not divisible by 2 and 3")
