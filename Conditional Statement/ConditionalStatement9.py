"""Write a program to check whether the last digit of a number( entered by user ) is divisible by 3 or not."""

number=int(input("Enter a number: "))

lastdigit= number % 10
print(lastdigit)
if lastdigit % 3 == 0:
    print(number, " is divisible by 3")
else:
    print(number, " is not divisible by 3")
